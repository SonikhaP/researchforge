"""Input validation and rate-limiting guards for all agent entry points."""

import re
import time
from collections import defaultdict
from functools import wraps

# Simple in-process rate limiter: max N calls per window (seconds)
_rate_store: dict[str, list[float]] = defaultdict(list)

MAX_QUERY_LENGTH = 500
MAX_CALLS = 10
WINDOW_SECONDS = 60


class SecurityError(ValueError):
    pass


def sanitize_query(query: str) -> str:
    """Strip control characters and enforce length cap."""
    if not query or not query.strip():
        raise SecurityError("Query must not be empty.")
    cleaned = re.sub(r"[\x00-\x1f\x7f]", " ", query).strip()
    if len(cleaned) > MAX_QUERY_LENGTH:
        raise SecurityError(
            f"Query exceeds {MAX_QUERY_LENGTH} characters. Please shorten it."
        )
    return cleaned


def rate_limit(key: str = "global") -> None:
    """Raise SecurityError if the call rate for `key` exceeds MAX_CALLS/WINDOW_SECONDS."""
    now = time.monotonic()
    calls = _rate_store[key]
    _rate_store[key] = [t for t in calls if now - t < WINDOW_SECONDS]
    if len(_rate_store[key]) >= MAX_CALLS:
        raise SecurityError(
            f"Rate limit reached ({MAX_CALLS} requests per {WINDOW_SECONDS}s). "
            "Please wait before submitting another query."
        )
    _rate_store[key].append(now)


def guarded(fn):
    """Decorator: sanitize first positional str arg and apply rate limiting."""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        rate_limit()
        if args:
            args = (sanitize_query(str(args[0])),) + args[1:]
        return fn(*args, **kwargs)
    return wrapper
