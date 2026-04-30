#!/usr/bin/env python3
# File: src/scitex_etc/__init__.py

"""
Utility functions for miscellaneous tasks.

This module provides utility functions that don't fit into other categories,
such as keyboard input handling for interactive programs.
"""

from . import wait_key as _wait_key_mod
from .wait_key import count
from .wait_key import wait_key as _wait_key_func

# Expose the submodule (not the function) so that `scitex_etc.wait_key`
# resolves to the module — required for `from scitex_etc.wait_key import wait_key`
# and `patch("scitex_etc.wait_key.readchar...")` to work.
wait_key = _wait_key_mod

__all__ = ["wait_key", "count"]

# EOF
