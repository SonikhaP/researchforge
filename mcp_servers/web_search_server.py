"""
MCP Server: Web Search Tools
Run standalone:  python mcp_servers/web_search_server.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from mcp.server.fastmcp import FastMCP
from tools.web_search_tools import web_search, format_web_results_as_markdown
from utils.security import sanitize_query, SecurityError

mcp = FastMCP("researchforge-websearch")


@mcp.tool()
def search_web(query: str, num_results: int = 5) -> str:
    """Search the web for current information on a topic.

    Args:
        query: Search terms or question.
        num_results: Number of results to return (1–10).
    """
    try:
        clean = sanitize_query(query)
    except SecurityError as e:
        return f"Error: {e}"

    num_results = max(1, min(10, num_results))
    results = web_search(clean, num_results)
    return format_web_results_as_markdown(results)


if __name__ == "__main__":
    mcp.run(transport="stdio")
