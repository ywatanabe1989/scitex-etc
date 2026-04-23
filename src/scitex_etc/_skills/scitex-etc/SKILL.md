---
name: scitex-etc
description: Miscellaneous SciTeX utilities — terminal single-keypress helpers for interactive scripts. Public API (2 symbols) — `wait_key()` (block until any key is pressed; returns the character or key code) and `count()` (read keys in a loop and return tallies; useful for quick manual-labeling or progress scripts in terminals). No CLI, no MCP tools, intentionally minimal grab-bag surface. Drop-in replacement for `input()` (which requires Enter), hand-rolled `termios`+`tty.setraw()` recipes for unbuffered stdin, the `getch`/`getkey`/`readchar` PyPI packages, and bespoke keypress-tallying loops in experiment-control scripts. Use whenever the user asks to "pause the script until the user presses a key", "read a keypress without Enter", "implement a simple manual-count loop via keypresses", or mentions `wait_key`, `scitex.etc`, getch-style input.
user-invocable: false
primary_interface: python
---

# scitex-etc

> **Primary interface: Python API.** Import in scripts/notebooks — CLI & MCP are thin wrappers over the Python functions.

Tiny grab-bag package. Current surface: two functions for reading a single
keypress in interactive terminal programs. This package is intentionally minimal;
do not expect a broad API.

## Installation & import (two equivalent paths)

The same module is reachable via two install paths. Both forms work at
runtime; which one a user has depends on their install choice.

```python
# Standalone — pip install scitex-etc
import scitex_etc
scitex_etc.wait_key(...)

# Umbrella — pip install scitex
import scitex.etc
scitex.etc.wait_key(...)
```

`pip install scitex-etc` alone does NOT expose the `scitex` namespace;
`import scitex.etc` raises `ModuleNotFoundError`. To use the
`scitex.etc` form, also `pip install scitex`.

See [../../general/02_interface-python-api.md] for the ecosystem-wide
rule and empirical verification table.

## Sub-skills

- [01_quick-start.md](01_quick-start.md) — install, import, two usage snippets
- [02_python-api.md](02_python-api.md) — public functions with signatures

No CLI, no MCP tools, no additional modules.
