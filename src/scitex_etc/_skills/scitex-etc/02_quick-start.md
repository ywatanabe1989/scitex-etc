---
description: |
  [TOPIC] scitex-etc Quick start
  [DETAILS] wait_key(p, ...) blocks until 'q' pressed then terminates process p; count(...) prints an incrementing counter forever.
tags: [scitex-etc-quick-start]
---

# Quick Start

## Run a counter and stop it by pressing 'q'

```python
import multiprocessing
from scitex_etc import wait_key, count

p = multiprocessing.Process(target=count)
p.start()
wait_key(p)  # Blocks until 'q' is pressed, then terminates the process
```

## Notes

- `wait_key` reads individual keypresses without requiring Enter. Runs until
  the user presses ``q``, then calls ``p.terminate()``.
- `count` prints an incrementing number once per second. It runs forever
  and must be stopped externally (e.g. via ``wait_key`` in another process).
- Both functions accept optional keyword-only arguments (``printer``,
  ``read_key``, ``sleeper``) as injectable test seams.

## Next

- [03_python-api.md](03_python-api.md) — public functions with signatures
- [SKILL.md](SKILL.md) — overview
