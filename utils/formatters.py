"""Markdown and text formatting helpers."""

import re


def truncate(text: str, max_chars: int = 3000) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "\n\n*[truncated for context window]*"


def clean_markdown(text: str) -> str:
    """Remove excessive blank lines from LLM output."""
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def section(title: str, body: str) -> str:
    return f"## {title}\n\n{body}\n"


def bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)
