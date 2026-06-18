---
name: scitex-etc
description: |
  [WHAT] Miscellaneous SciTeX utilities — count_grids/yield_grids for parameter-grid iteration, search for substring/regex matching, and media.render for media-reference detection/display (see scitex-etc-media).
  [WHEN] Sweeping over a parameter grid, doing a small pattern search over text, or detecting/classifying/displaying media references in chat-pane / terminal / markdown contexts.
  [HOW] `from scitex_etc import count_grids, yield_grids, search` for the helpers; `from scitex_etc.media import render` for media (see the scitex-etc-media sub-skill).
tags: [scitex-etc]
primary_interface: python
interfaces:
  python: 3
  cli: 1
  mcp: 1
  skills: 1
  http: 0
---

# scitex-etc

> **Interfaces:** Python ⭐⭐⭐ (primary) · CLI ⭐ · MCP ⭐ · Skills ⭐ · Hook — · HTTP —

Tiny grab-bag package for cross-cutting helpers that don't fit a
domain-specific package:

- `count_grids(...)` / `yield_grids(...)` — combinatorial parameter-grid
  iteration.
- `search(pattern, text)` — small substring/regex search helper.
- `media.render` — chat-pane / terminal / markdown media-reference
  detection & display (see the `scitex-etc-media` sub-skill).

## Installation & import (two equivalent paths)

The same module is reachable via two install paths. Both forms work at
runtime; which one a user has depends on their install choice.

```python
# Standalone — pip install scitex-etc
import scitex_etc
scitex_etc.count_grids(...)

# Umbrella — pip install scitex
import scitex.etc
scitex.etc.count_grids(...)
```

`pip install scitex-etc` alone does NOT expose the `scitex` namespace;
`import scitex.etc` raises `ModuleNotFoundError`. To use the
`scitex.etc` form, also `pip install scitex`.

See [../../general/02_interface-python-api.md] for the ecosystem-wide
rule and empirical verification table.

## Sub-skills

- [01_installation.md](01_installation.md) — pip install + smoke verify
- [02_quick-start.md](02_quick-start.md) — count_grids / search / media examples
- [03_python-api.md](03_python-api.md) — public functions with signatures
- [../scitex-etc-media/SKILL.md](../scitex-etc-media/SKILL.md) — media.render skill bundle
