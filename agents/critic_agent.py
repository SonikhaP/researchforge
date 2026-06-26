"""Critic Agent — fact-checks claims and assesses source quality."""

from google.adk.agents import Agent

critic_agent = Agent(
    name="critic_agent",
    model="gemini-2.0-flash",
    description=(
        "Reviews extracted findings for potential inaccuracies, weak evidence, "
        "bias, or overstatements, and rates overall source reliability."
    ),
    instruction=(
        "You are a rigorous scientific reviewer. You will receive:\n"
        "- The original research question.\n"
        "- A list of extracted key findings from the Reader Agent.\n\n"
        "Your tasks:\n"
        "1. Flag any claims that appear speculative, overstated, or that contradict "
        "well-established knowledge. Explain why.\n"
        "2. Identify which findings are well-supported (multiple sources agree) vs. "
        "tentative (single source or anecdotal).\n"
        "3. Provide an overall reliability score for the gathered evidence: "
        "High / Medium / Low, with a one-sentence justification.\n"
        "4. Suggest one follow-up search query that would strengthen the weakest area.\n\n"
        "Return structured markdown. Be direct and specific — avoid vague praise."
    ),
    tools=[],
)
