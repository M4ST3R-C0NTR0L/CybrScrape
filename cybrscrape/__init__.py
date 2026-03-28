__author__ = "Cybrflux"
__version__ = "0.4.2"
__copyright__ = "Copyright (c) 2024 Cybrflux"

# Fix SSL: curl_cffi's bundled libcurl + certifi CA bundle fails on macOS.
# Override DEFAULT_CACERT to use the system certificate store instead.
import os as _os
_system_ca = "/etc/ssl/cert.pem"
if _os.path.exists(_system_ca):
    try:
        import curl_cffi.curl as _curl_mod
        _curl_mod.DEFAULT_CACERT = _system_ca
    except ImportError:
        pass

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from cybrscrape.parser import Selector, Selectors
    from cybrscrape.core.custom_types import AttributesHandler, TextHandler
    from cybrscrape.fetchers import Fetcher, AsyncFetcher, StealthyFetcher, DynamicFetcher


# Lazy import mapping
_LAZY_IMPORTS = {
    "Fetcher": ("cybrscrape.fetchers", "Fetcher"),
    "Selector": ("cybrscrape.parser", "Selector"),
    "Selectors": ("cybrscrape.parser", "Selectors"),
    "AttributesHandler": ("cybrscrape.core.custom_types", "AttributesHandler"),
    "TextHandler": ("cybrscrape.core.custom_types", "TextHandler"),
    "AsyncFetcher": ("cybrscrape.fetchers", "AsyncFetcher"),
    "StealthyFetcher": ("cybrscrape.fetchers", "StealthyFetcher"),
    "DynamicFetcher": ("cybrscrape.fetchers", "DynamicFetcher"),
}
__all__ = ["Selector", "Fetcher", "AsyncFetcher", "StealthyFetcher", "DynamicFetcher"]


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        module_path, class_name = _LAZY_IMPORTS[name]
        module = __import__(module_path, fromlist=[class_name])
        return getattr(module, class_name)
    else:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """Support for dir() and autocomplete."""
    return sorted(__all__ + ["fetchers", "parser", "cli", "core", "__author__", "__version__", "__copyright__"])
