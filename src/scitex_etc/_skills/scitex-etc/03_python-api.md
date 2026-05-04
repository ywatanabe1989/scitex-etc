---
description: |
  [TOPIC] scitex-etc Python API
  [DETAILS] Two public callables — wait_key() (block on single keypress) and count() (tally loop).
tags: [scitex-etc-python-api]
---

# Python API

## Imports

```python
from scitex_etc import wait_key, count
```

The submodule itself is also exposed:

```python
import scitex_etc
scitex_etc.wait_key            # the submodule (needed for monkeypatching)
scitex_etc.wait_key.wait_key   # the function inside it
```

## `wait_key() -> str`

Block until a single key is pressed; return the character. No need to
press Enter. POSIX implementation uses termios cbreak mode; Windows uses
`msvcrt.getch`.

```python
from scitex_etc import wait_key
ch = wait_key()        # 'a', 'q', '\r', ...
```

## `count(stop_keys=("q",)) -> int`

Run a manual tally loop: each non-stop keypress increments a counter;
pressing any key in `stop_keys` ends the loop and returns the total.
Useful for hand-tagging events while watching a recording.

```python
from scitex_etc import count
n = count(stop_keys=("q", "\x1b"))   # also Esc
```

## Two import paths

```python
import scitex_etc        # standalone
import scitex.etc        # umbrella (requires `pip install scitex`)
```

The submodule is intentionally minimal — do not expect the surface to
grow. New unrelated utilities should live in dedicated `scitex-*`
packages.
