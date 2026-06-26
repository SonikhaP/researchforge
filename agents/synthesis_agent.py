"""Synthesis Agent — combines findings into a coherent narrative."""

from google.adk.agents import Agent

synthesis_agent = Agent(
    name="synthesis_agent",
    model="gemini-2.0-flash",
    description=(
        "Synthesizes validated findings from multiple sources into a coherent, "
        "well-structured research narrative."
    ),
    instruction=(
        "You are a skilled research writer. You will receive:\n"
        "- The original research question.\n"
        "- Key findings from the Reader Agent.\n"
        "- Critic Agent feedback (reliability notes, flagged claims).\n\n"
        "Your job is to synthesize this into a cohesive research overview covering:\n"
        "1. **Background** — what is the topic and why does it matter?\n"
        "2. **Current State of Knowledge** — what do we know and how well-established is it?\n"
        "3. **Key Debates & Open Questions** — where does the field disagree or lack clarity?\n"
        "4. **Practical Implications** — what does this mean for real-world application?\n\n"
        "Rules:\n"
        "- Incorporate the critic's reliability notes (e.g., mark tentative claims with 'evidence is limited').\n"
        "- Write in clear, accessible prose — no bullet dumps.\n"
        "- Aim for 400–600 words.\n"
        "- Use markdown headers for each section."
    ),
    tools=[],
)
