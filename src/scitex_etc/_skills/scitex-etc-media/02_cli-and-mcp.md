---
description: Use scitex_etc.media.render from the command line and as MCP tools (render_show, render_detect, render_classify).
---

# scitex_etc.media.render — CLI and MCP

## CLI

The `render` submodule ships a `__main__` entry point:

```bash
python -m scitex_etc.media.render show figure.png --target terminal
python -m scitex_etc.media.render show figure.png --target markdown
python -m scitex_etc.media.render classify data.csv
python -m scitex_etc.media.render detect "Saved /proj/fig.png" --root /proj
```

Subcommands:

| Command | Arguments | Output |
|---------|-----------|--------|
| `show` | `path`, `-t/--target {terminal,chat,markdown}`, `--root`, `--alt` | OSC escape (terminal), or the formatted string printed to stdout |
| `classify` | `path` | JSON MediaRef dict, or `null` |
| `detect` | `text`, `--root` (required) | JSON list of MediaRef dicts |

## MCP

`scitex_etc.media.render.mcp_server` exposes the same surface as MCP tools when
`fastmcp` is installed. The module imports cleanly without `fastmcp`
(`FASTMCP_AVAILABLE` is then `False` and `mcp` is `None`).

| Tool | Wraps | Returns |
|------|-------|---------|
| `render_show(path, target, root_path, alt)` | `render.show` | formatted target string |
| `render_detect(text, root_path)` | `render.detect` | JSON list of MediaRef dicts |
| `render_classify(path)` | `render.classify` | JSON MediaRef dict or `"null"` |

Run the server over stdio:

```bash
python -m scitex_etc.media.render.mcp_server   # requires: pip install fastmcp
```

Or programmatically:

```python
from scitex_etc.media.render import mcp_server

if mcp_server.FASTMCP_AVAILABLE:
    mcp_server.mcp.run(transport="stdio")
```
