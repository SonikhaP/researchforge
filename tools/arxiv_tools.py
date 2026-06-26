"""arXiv search and paper-fetching tools exposed to agents."""

import arxiv
from utils.formatters import truncate


def search_arxiv(query: str, max_results: int = 5) -> list[dict]:
    """Search arXiv for academic papers matching the query.

    Returns a list of dicts with keys: title, authors, summary, url, published.
    """
    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance,
    )
    results = []
    for paper in client.results(search):
        results.append(
            {
                "title": paper.title,
                "authors": [a.name for a in paper.authors[:4]],
                "summary": truncate(paper.summary, 800),
                "url": paper.entry_id,
                "published": paper.published.strftime("%Y-%m-%d") if paper.published else "unknown",
            }
        )
    return results


def format_papers_as_markdown(papers: list[dict]) -> str:
    """Convert paper list to a readable markdown block."""
    if not papers:
        return "*No papers found.*"
    lines = []
    for i, p in enumerate(papers, 1):
        authors = ", ".join(p["authors"]) if p["authors"] else "Unknown"
        lines.append(
            f"**{i}. {p['title']}**  \n"
            f"*{authors} — {p['published']}*  \n"
            f"{p['summary']}  \n"
            f"[arXiv link]({p['url']})\n"
        )
    return "\n---\n".join(lines)
