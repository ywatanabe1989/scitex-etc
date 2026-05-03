---
description: |
  [TOPIC] Quick Start
  [DETAILS] Install, import, and two usage snippets covering wait_key and count.
tags: [scitex-etc-quick-start]
---

<!-- 01_quick-start.md -->

# scitex-etc — Quick Start

## Install

```bash
pip install scitex-etc
```

## Import

```python
import scitex_etc
```

## Usage

### Block until any key is pressed

```python
from scitex_etc import wait_key

print("Press any key to continue...")
wait_key()
print("Got it!")
```

### Count keypresses interactively

```python
from scitex_etc import count

# Returns an integer count after user finishes input.
n = count()
print(f"You pressed {n} keys")
```

That is the entire public surface. If you need richer interactive input, use
`readchar`, `prompt_toolkit`, or `curses` directly.
