"""
MCP Server: arXiv Research Tools
Run standalone:  python mcp_servers/arxiv_server.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from mcp.server.fastmcp import FastMCP
from tools.arxiv_tools import search_arxiv, format_papers_as_markdown
from utils.security import sanitize_query, SecurityError

mcp = FastMCP("researchforge-arxiv")


@mcp.tool()
def arxiv_search(query: str, max_results: int = 5) -> str:
    """Search arXiv academic papers by keyword or topic.

    Args:
        query: The research topic or keywords to search for.
        max_results: Number of papers to return (1–10).
    """
    try:
        clean = sanitize_query(query)
    except SecurityError as e:
        return f"Error: {e}"

    max_results = max(1, min(10, max_results))
    papers = search_arxiv(clean, max_results)
    return format_papers_as_markdown(papers)


@mcp.tool()
def arxiv_recent(topic: str, max_results: int = 3) -> str:
    """Fetch the most recent arXiv papers on a topic.

    Args:
        topic: Research area or field name.
        max_results: Number of papers to return (1–10).
    """
    try:
        clean = sanitize_query(topic)
    except SecurityError as e:
        return f"Error: {e}"

    import arxiv as _arxiv
    from utils.formatters import truncate

    client = _arxiv.Client()
    search = _arxiv.Search(
        query=clean,
        max_results=max(1, min(10, max_results)),
        sort_by=_arxiv.SortCriterion.SubmittedDate,
    )
    papers = []
    for p in client.results(search):
        papers.append(
            {
                "title": p.title,
                "authors": [a.name for a in p.authors[:3]],
                "summary": truncate(p.summary, 600),
                "url": p.entry_id,
                "published": p.published.strftime("%Y-%m-%d") if p.published else "unknown",
            }
        )
    return format_papers_as_markdown(papers)


if __name__ == "__main__":
    mcp.run(transport="stdio")
