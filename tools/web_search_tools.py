"""Web search tools using the Serper.dev API."""

import os
import httpx
from utils.formatters import truncate

SERPER_URL = "https://google.serper.dev/search"


def web_search(query: str, num_results: int = 5) -> list[dict]:
    """Search the web via Serper and return structured results.

    Returns list of dicts with keys: title, snippet, url.
    Falls back gracefully if the API key is missing.
    """
    api_key = os.getenv("SERPER_API_KEY", "")
    if not api_key:
        return [{"title": "No web search", "snippet": "SERPER_API_KEY not set.", "url": ""}]

    headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
    payload = {"q": query, "num": num_results}

    try:
        response = httpx.post(SERPER_URL, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        results = []
        for item in data.get("organic", [])[:num_results]:
            results.append(
                {
                    "title": item.get("title", ""),
                    "snippet": truncate(item.get("snippet", ""), 400),
                    "url": item.get("link", ""),
                }
            )
        return results
    except Exception as exc:
        return [{"title": "Search error", "snippet": str(exc), "url": ""}]


def format_web_results_as_markdown(results: list[dict]) -> str:
    if not results:
        return "*No web results.*"
    lines = []
    for r in results:
        lines.append(f"**{r['title']}**  \n{r['snippet']}  \n[link]({r['url']})")
    return "\n\n".join(lines)
