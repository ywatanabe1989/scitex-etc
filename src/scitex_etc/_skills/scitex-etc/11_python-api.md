---
description: |
  [TOPIC] Python API (legacy)
  [DETAILS] Legacy API notes. Use 03_python-api.md instead. wait_key(p), count(...) signatures.
tags: [scitex-etc-python-api]
---

<!-- 02_python-api.md (legacy, replaced by 03_python-api.md) -->

# scitex-etc — Python API

All public symbols are in `scitex_etc.__all__`:

| Symbol | Kind | One-liner |
|--------|------|-----------|
| `wait_key` | function | Block until ``q`` pressed, then terminate process. |
| `count` | function | Print incrementing counter forever (1 per second). |

## Signatures

```python
wait_key(p, *, read_key=None, printer=print)
count(*, printer=print, sleeper=time.sleep)
```

Both live in `scitex_etc/wait_key.py`. See the source for the full docstrings
and test-seam details — they accept injectable keyword-only arguments for
testing and have no positional arguments beyond ``p``.
