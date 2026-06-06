---
description: |
  [TOPIC] scitex-etc Python API
  [DETAILS] Public callables — count_grids, yield_grids, search — plus the media submodule (see scitex-etc-media skill).
tags: [scitex-etc-python-api]
---

# Python API

## Imports

```python
from scitex_etc import count_grids, yield_grids, search
from scitex_etc.media import render  # detect / classify / show
```

## `count_grids(grid)`

Return the total number of parameter combinations in a grid dict.

```python
from scitex_etc import count_grids
count_grids({"lr": [1e-3, 1e-2], "batch": [32, 64]})  # 4
```

## `yield_grids(grid)`

Yield each parameter combination of a grid dict as its own dict.

```python
from scitex_etc import yield_grids
for combo in yield_grids({"lr": [1e-3, 1e-2], "batch": [32, 64]}):
    ...
```

## `search(pattern, text)`

Small substring/regex search helper.

```python
from scitex_etc import search
search(r"error|warn", "WARN something")
```

## `media.render`

See the [scitex-etc-media](../scitex-etc-media/SKILL.md) skill bundle:
`render.classify(path)`, `render.detect(text, root_path=...)`,
`render.show(path, target=...)`, and the
`python -m scitex_etc.media.render` CLI / MCP server.

## Two import paths

```python
import scitex_etc        # standalone
import scitex.etc        # umbrella (requires `pip install scitex`)
```
