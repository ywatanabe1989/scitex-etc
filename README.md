# scitex-etc

Interactive keyboard input utilities for the SciTeX ecosystem.

## Problem and Solution


| # | Problem | Solution |
|---|---------|----------|
| 1 | **Scripts that pause for a keypress need raw-stdin + termios gymnastics** -- 15 lines of OS-dependent boilerplate | **`wait_key()` / `count()`** -- one import; handles Linux/macOS/Windows; falls back cleanly when stdin isn't a TTY |

## Installation

```bash
pip install scitex-etc
```

## Usage

```python
from scitex_etc import wait_key, count

key = wait_key()  # Wait for a single keypress
count(5)  # Countdown timer
```

## License

AGPL-3.0
