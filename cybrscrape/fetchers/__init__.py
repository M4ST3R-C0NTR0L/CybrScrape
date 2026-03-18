from typing import TYPE_CHECKING, Any
from cybrscrape.engines.toolbelt import ProxyRotator

if TYPE_CHECKING:
    from cybrscrape.fetchers.requests import Fetcher, AsyncFetcher, FetcherSession
    from cybrscrape.fetchers.chrome import DynamicFetcher, DynamicSession, AsyncDynamicSession
    from cybrscrape.fetchers.stealth_chrome import StealthyFetcher, StealthySession, AsyncStealthySession


# Lazy import mapping
_LAZY_IMPORTS = {
    "Fetcher": ("cybrscrape.fetchers.requests", "Fetcher"),
    "AsyncFetcher": ("cybrscrape.fetchers.requests", "AsyncFetcher"),
    "FetcherSession": ("cybrscrape.fetchers.requests", "FetcherSession"),
    "DynamicFetcher": ("cybrscrape.fetchers.chrome", "DynamicFetcher"),
    "DynamicSession": ("cybrscrape.fetchers.chrome", "DynamicSession"),
    "AsyncDynamicSession": ("cybrscrape.fetchers.chrome", "AsyncDynamicSession"),
    "StealthyFetcher": ("cybrscrape.fetchers.stealth_chrome", "StealthyFetcher"),
    "StealthySession": ("cybrscrape.fetchers.stealth_chrome", "StealthySession"),
    "AsyncStealthySession": ("cybrscrape.fetchers.stealth_chrome", "AsyncStealthySession"),
}

__all__ = [
    "Fetcher",
    "AsyncFetcher",
    "ProxyRotator",
    "FetcherSession",
    "DynamicFetcher",
    "DynamicSession",
    "AsyncDynamicSession",
    "StealthyFetcher",
    "StealthySession",
    "AsyncStealthySession",
]


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        module_path, class_name = _LAZY_IMPORTS[name]
        module = __import__(module_path, fromlist=[class_name])
        return getattr(module, class_name)
    else:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """Support for dir() and autocomplete."""
    return sorted(list(_LAZY_IMPORTS.keys()))
