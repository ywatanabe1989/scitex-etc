---
name: scitex-etc-media
description: |
  [WHAT] Media handling for SciTeX — detect file paths in text (render.detect), classify a file by media type (render.classify), and render a file to terminal/chat/markdown (render.show).
  [WHEN] Scanning tool output for produced figures/data files, deciding how to display a file inline (terminal OSC overlay, AI chat pane, or markdown embed), or mapping a filename extension to a media category.
  [HOW] `from scitex_etc.media import render` — call `render.detect(text, root_path=...)`, `render.classify(path)`, or `render.show(path, target=...)`.
tags: [scitex-etc, media]
primary_interface: python
interfaces:
  python: 3
  cli: 1
  mcp: 1
  skills: 1
  http: 0
---

# scitex-etc-media

> **Interfaces:** Python ⭐⭐⭐ (primary) · CLI ⭐ · MCP ⭐ · Skills ⭐ · Hook — · HTTP —

`scitex_etc.media` provides the `render` submodule: detect media file
references in text, classify a file by its extension, and format a file for a
display target (terminal OSC overlay, AI chat pane, or markdown embed).

```python
from scitex_etc.media import render

render.classify("fig.png")              # {"type": "image", "path": "fig.png", "ext": ".png"}
render.detect(out, root_path="/proj")   # [{"type": "image", "path": "fig.png", "ext": ".png"}]
render.show("fig.png", target="markdown")  # "![fig.png](fig.png)"
```

Reachable via two install paths: `pip install scitex-etc` →
`from scitex_etc.media import render`; `pip install scitex` →
`from scitex.media import render` (umbrella alias).

## Sub-skills

- [01_render-detect-classify-show.md](01_render-detect-classify-show.md) — detect / classify / show with examples
- [02_cli-and-mcp.md](02_cli-and-mcp.md) — `python -m scitex_etc.media.render` CLI + MCP tools
