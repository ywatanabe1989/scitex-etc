---
description: |
  [TOPIC] Python API
  [DETAILS] Public functions wait_key() and count() with signatures.
tags: [scitex-etc-python-api]
---

<!-- 02_python-api.md -->

# scitex-etc — Python API

All public symbols are in `scitex_etc.__all__`:

| Symbol | Kind | One-liner |
|--------|------|-----------|
| `wait_key` | function | Block until the user presses any key; returns the key. |
| `count` | function | Interactive keypress counter, returns integer. |

## Signatures

```python
wait_key() -> str | None
count() -> int
```

Both live in `scitex_etc/wait_key.py`. See the source for the full docstrings
and terminal-handling details — they use `termios`/`msvcrt` directly and have
no keyword arguments.
