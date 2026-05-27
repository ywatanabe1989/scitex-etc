---
description: |
  [TOPIC] scitex-etc Python API
  [DETAILS] Two public callables — wait_key(p, ...) (block until 'q', terminate process) and count(...) (infinite counter).
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

## `wait_key(p, *, read_key=None, printer=print)`

Block until the user presses ``q``, then terminate process ``p``.
Echoes each key as it is pressed; on ``q`` prints a notice and calls
``p.terminate()``.

```python
import multiprocessing
from scitex_etc import wait_key, count

p = multiprocessing.Process(target=count)
p.start()
wait_key(p)  # 'q' → prints "q was pressed." and terminates p
```

Parameters:
- ``p`` — A process-like object exposing ``terminate()``.
- ``read_key`` (optional) — Zero-arg callable returning the next key as a
  string. Defaults to ``readchar.readchar``. Injectable test seam.
- ``printer`` (optional) — Output sink. Defaults to ``print``. Injectable
  test seam.

## `count(*, printer=print, sleeper=time.sleep)`

Print an incrementing counter forever, sleeping 1s between values.

```python
from scitex_etc import count
# Runs until the process is terminated externally
```

Parameters:
- ``printer`` (optional) — Output sink. Defaults to ``print``. Injectable
  test seam.
- ``sleeper`` (optional) — One-arg sleep callable. Defaults to
  ``time.sleep``. Injectable so tests can run without real delay.

## Two import paths

```python
import scitex_etc        # standalone
import scitex.etc        # umbrella (requires `pip install scitex`)
```

The submodule is intentionally minimal — do not expect the surface to
grow. New unrelated utilities should live in dedicated `scitex-*`
packages.
