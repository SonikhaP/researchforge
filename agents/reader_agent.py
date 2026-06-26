"""Reader Agent — extracts key findings and concepts from raw source material."""

from google.adk.agents import Agent

reader_agent = Agent(
    name="reader_agent",
    model="gemini-2.0-flash",
    description=(
        "Reads raw source material (paper abstracts, web snippets) and extracts "
        "key findings, definitions, methodologies, and notable claims."
    ),
    instruction=(
        "You are a careful academic reader. You will receive a block of raw source material "
        "(paper abstracts and web snippets). Your job is to:\n"
        "1. Identify the 5–8 most important concepts, findings, or claims across all sources.\n"
        "2. Note any conflicting viewpoints between sources.\n"
        "3. Flag any gaps — important sub-questions the sources do not address.\n"
        "4. Return your output as structured markdown with clear section headers:\n"
        "   - Key Findings\n"
        "   - Important Concepts & Definitions\n"
        "   - Conflicting Viewpoints (if any)\n"
        "   - Gaps & Open Questions\n"
        "Be concise. Do not copy-paste raw text — paraphrase and synthesize."
    ),
    tools=[],
)
