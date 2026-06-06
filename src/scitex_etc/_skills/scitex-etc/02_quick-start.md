---
description: |
  [TOPIC] scitex-etc Quick start
  [DETAILS] count_grids/yield_grids iterate parameter combinations; search does substring/regex matching; media.render detects/classifies/displays media references.
tags: [scitex-etc-quick-start]
---

# Quick Start

## Iterate a parameter grid

```python
from scitex_etc import count_grids, yield_grids

grid = {"lr": [1e-3, 1e-2], "batch": [32, 64]}
print(count_grids(grid))                # 4
for combo in yield_grids(grid):
    print(combo)
```

## Pattern search

```python
from scitex_etc import search

hits = search(r"error|warn", "log line: WARN something")
```

## Media reference detection

```python
from scitex_etc.media import render

render.classify("fig.png")                 # {"type": "image", ...}
render.detect(out, root_path="/proj")      # list of detected media refs
render.show("fig.png", target="markdown")  # "![fig.png](fig.png)"
```

See [../scitex-etc-media/01_render-detect-classify-show.md](../scitex-etc-media/01_render-detect-classify-show.md)
for the full media surface.

## Next

- [03_python-api.md](03_python-api.md) — public functions with signatures
- [SKILL.md](SKILL.md) — overview
