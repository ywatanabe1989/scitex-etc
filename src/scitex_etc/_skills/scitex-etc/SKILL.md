---
name: scitex-etc
description: Miscellaneous SciTeX utilities — interactive keyboard input helpers that don't fit elsewhere. Use when a script needs a blocking keypress or simple key counter.
user-invocable: false
---

# scitex-etc

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
