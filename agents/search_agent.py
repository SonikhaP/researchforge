"""Search Agent — finds academic papers and web sources for a research topic."""

from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from tools.arxiv_tools import search_arxiv, format_papers_as_markdown
from tools.web_search_tools import web_search, format_web_results_as_markdown


def _arxiv_search_tool(query: str, max_results: int = 5) -> str:
    """Search arXiv for academic papers on the given topic."""
    papers = search_arxiv(query, max_results)
    return format_papers_as_markdown(papers)


def _web_search_tool(query: str, num_results: int = 5) -> str:
    """Search the web for recent articles and resources on the given topic."""
    results = web_search(query, num_results)
    return format_web_results_as_markdown(results)


search_agent = Agent(
    name="search_agent",
    model="gemini-2.0-flash",
    description=(
        "Searches arXiv and the web to gather relevant academic papers and "
        "web sources for a given research topic."
    ),
    instruction=(
        "You are a research librarian. Given a research topic, use the available tools to:\n"
        "1. Search arXiv for 5 relevant academic papers.\n"
        "2. Search the web for 5 relevant recent articles or resources.\n"
        "Return a combined list of sources in markdown, clearly separating academic papers "
        "from web results. Include titles, author/date info, brief summaries, and URLs."
    ),
    tools=[
        FunctionTool(_arxiv_search_tool),
        FunctionTool(_web_search_tool),
    ],
)
