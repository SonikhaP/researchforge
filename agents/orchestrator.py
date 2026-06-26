"""
Orchestrator — drives the full ResearchForge multi-agent pipeline.

Pipeline:
  1. Search Agent   → gathers papers + web sources
  2. Reader Agent   → extracts key findings
  3. Critic Agent   → validates and scores evidence
  4. Synthesis Agent → builds coherent narrative
  5. Report Writer  → produces the final report
"""

import asyncio
import os
import time
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.models.google_llm import _ResourceExhaustedError
from google import genai
from google.genai.errors import ClientError

from agents.search_agent import search_agent
from agents.reader_agent import reader_agent
from agents.critic_agent import critic_agent
from agents.synthesis_agent import synthesis_agent
from agents.report_writer import report_writer_agent
from utils.security import sanitize_query, rate_limit, SecurityError
from utils.formatters import clean_markdown


def _get_client() -> genai.Client:
    api_key = os.getenv("GOOGLE_API_KEY", "")
    if not api_key:
        raise EnvironmentError("GOOGLE_API_KEY is not set. Add it to your .env file.")
    return genai.Client(api_key=api_key)


async def _run_agent(agent: Agent, prompt: str, session_service, app_name: str, retries: int = 3) -> str:
    """Run a single ADK agent and return its text response. Retries on 429."""
    runner = Runner(
        agent=agent,
        app_name=app_name,
        session_service=session_service,
    )
    session = await session_service.create_session(
        app_name=app_name,
        user_id="researchforge_user",
    )
    from google.genai.types import Content, Part
    message = Content(role="user", parts=[Part(text=prompt)])

    for attempt in range(retries):
        try:
            final_response = ""
            async for event in runner.run_async(
                user_id="researchforge_user",
                session_id=session.id,
                new_message=message,
            ):
                if event.is_final_response() and event.content:
                    for part in event.content.parts:
                        if hasattr(part, "text") and part.text:
                            final_response += part.text
            return clean_markdown(final_response)
        except (_ResourceExhaustedError, ClientError) as e:
            is_429 = (isinstance(e, _ResourceExhaustedError) or
                      (isinstance(e, ClientError) and e.code == 429))
            if is_429 and attempt < retries - 1:
                wait = 40 * (attempt + 1)
                await asyncio.sleep(wait)
            else:
                raise


async def run_pipeline(query: str, progress_callback=None) -> dict:
    """
    Execute the full research pipeline for `query`.

    Args:
        query: The research question from the user.
        progress_callback: Optional callable(step: int, label: str) for UI updates.

    Returns:
        dict with keys: sources, findings, critique, synthesis, report, query
    """
    try:
        clean_query = sanitize_query(query)
        rate_limit("pipeline")
    except SecurityError as e:
        return {"error": str(e)}

    session_service = InMemorySessionService()

    def _progress(step: int, label: str):
        if progress_callback:
            progress_callback(step, label)

    # Step 1 — Search
    _progress(1, "Searching arXiv and the web...")
    sources = await _run_agent(
        search_agent,
        f"Research topic: {clean_query}",
        session_service,
        "search",
    )

    # Step 2 — Read
    _progress(2, "Extracting key findings...")
    findings = await _run_agent(
        reader_agent,
        f"Research question: {clean_query}\n\nSource material:\n{sources}",
        session_service,
        "reader",
    )

    # Step 3 — Critique
    _progress(3, "Fact-checking and assessing reliability...")
    critique = await _run_agent(
        critic_agent,
        f"Research question: {clean_query}\n\nExtracted findings:\n{findings}",
        session_service,
        "critic",
    )

    # Step 4 — Synthesize
    _progress(4, "Synthesizing into a coherent narrative...")
    synthesis = await _run_agent(
        synthesis_agent,
        (
            f"Research question: {clean_query}\n\n"
            f"Key findings:\n{findings}\n\n"
            f"Critic feedback:\n{critique}"
        ),
        session_service,
        "synthesis",
    )

    # Step 5 — Write report
    _progress(5, "Writing the final report...")
    report = await _run_agent(
        report_writer_agent,
        (
            f"Research question: {clean_query}\n\n"
            f"Synthesized narrative:\n{synthesis}\n\n"
            f"Sources:\n{sources}\n\n"
            f"Reliability assessment:\n{critique}"
        ),
        session_service,
        "report_writer",
    )

    _progress(6, "Done!")
    return {
        "query": clean_query,
        "sources": sources,
        "findings": findings,
        "critique": critique,
        "synthesis": synthesis,
        "report": report,
    }


def run_research(query: str, progress_callback=None) -> dict:
    """Synchronous entry point — wraps the async pipeline."""
    return asyncio.run(run_pipeline(query, progress_callback))
