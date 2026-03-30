#!/usr/bin/env python3
# File: src/scitex_etc/__init__.py

"""
Utility functions for miscellaneous tasks.

This module provides utility functions that don't fit into other categories,
such as keyboard input handling for interactive programs.
"""

from .wait_key import count, wait_key

__all__ = ["wait_key", "count"]

# EOF
