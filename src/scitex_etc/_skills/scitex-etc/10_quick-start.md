---
description: |
  [TOPIC] Quick Start (legacy)
  [DETAILS] Legacy quick-start. Use 02_quick-start.md instead. wait_key(p) + count(...) usage with multiprocessing.
tags: [scitex-etc-quick-start]
---

<!-- 01_quick-start.md (legacy, replaced by 02_quick-start.md) -->

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

### Run a counter and stop it by pressing 'q'

```python
import multiprocessing
from scitex_etc import wait_key, count

p = multiprocessing.Process(target=count)
p.start()
wait_key(p)
```

That is the entire public surface. If you need richer interactive input, use
`readchar`, `prompt_toolkit`, or `curses` directly.
