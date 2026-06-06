#!/usr/bin/env python3
# File: src/scitex_etc/__init__.py

"""
SciTeX miscellaneous utility helpers.

Cross-cutting helpers that don't fit a domain-specific package:

- Combinatorial parameter-grid iteration (``count_grids`` / ``yield_grids``)
- ``search`` — small substring/pattern search helper.
- ``media`` — chat-pane / terminal / markdown media-reference detection
  & display (``media.render.{classify, detect, show, MEDIA_EXTENSIONS}``,
  plus a CLI and an MCP server). Ported from ``scitex.media`` per
  ADR-0001 (scitex-python repo).

Historical surface (removed in v0.3.0):

- ``wait_key`` / ``count``: moved to ``scitex-parallel`` (unified with
  ``scitex_gen.wait_key``).
"""

from __future__ import annotations

try:
    from importlib.metadata import version as _v, PackageNotFoundError

    try:
        __version__ = _v("scitex-etc")
    except PackageNotFoundError:
        __version__ = "0.0.0+local"
    del _v, PackageNotFoundError
except ImportError:  # pragma: no cover — only on ancient Pythons
    __version__ = "0.0.0+local"

from . import media  # noqa: F401  — media handling (detect/classify/show)
from ._grid import count_grids, yield_grids
from ._search import search

__all__ = [
    "__version__",
    "count_grids",
    "yield_grids",
    "search",
    "media",
]

# EOF
