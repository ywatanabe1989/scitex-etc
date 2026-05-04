---
description: |
  [TOPIC] scitex-etc Quick start
  [DETAILS] Single-keypress input — wait_key() blocks for any key, count() implements a tally loop.
tags: [scitex-etc-quick-start]
---

# Quick Start

## Pause until any key is pressed

```python
from scitex_etc import wait_key

print("Press any key to continue...")
wait_key()             # returns the character that was pressed
print("Continuing.")
```

Unlike `input()`, no Enter is required.

## Manual count loop

```python
from scitex_etc import count

# Increment a tally on each keypress; press q to quit
total = count(stop_keys=("q",))
print(f"Tallied: {total}")
```

## Notes

- Returns immediately on any key — no echo by default.
- POSIX-only behavior may differ in some non-TTY contexts (CI, redirected
  stdin); use a fallback when scripting non-interactively.

## Next

- [03_python-api.md](03_python-api.md) — public functions with signatures
- [SKILL.md](SKILL.md) — overview
