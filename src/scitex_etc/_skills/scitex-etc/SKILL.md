---
name: scitex-etc
description: |
  [WHAT] Miscellaneous SciTeX utilities — wait_key(p) blocks until 'q' pressed (terminates a process), count() prints an incrementing counter forever.
  [WHEN] Pausing a script until 'q' is typed to cleanly terminate a background process, implementing a simple counter loop with injectable test seams, or needing unbuffered keypress reading.
  [HOW] `from scitex_etc import wait_key, count` — call `wait_key(p)` to block on a process until 'q', `count(...)` to start an infinite counter.
tags: [scitex-etc]
primary_interface: python
interfaces:
  python: 3
  cli: 0
  mcp: 0
  skills: 1
  http: 0
---

# scitex-etc

> **Interfaces:** Python ⭐⭐⭐ (primary) · CLI — · MCP — · Skills ⭐ · Hook — · HTTP —

Tiny grab-bag package. Current surface: `wait_key(p)` — blocks reading keys
until ``q`` is pressed, then terminates a process — and `count()` — prints an
incrementing counter once per second forever. Both accept injectable
keyword-only test seams. This package is intentionally minimal; do not expect
a broad API.

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

- [01_installation.md](01_installation.md) — pip install + smoke verify
- [02_quick-start.md](02_quick-start.md) — wait_key + count examples
- [03_python-api.md](03_python-api.md) — public functions with signatures
- [10_quick-start.md](10_quick-start.md) — legacy quick-start (kept for context)
- [11_python-api.md](11_python-api.md) — legacy API notes (kept for context)

No CLI, no MCP tools, no additional modules.
