# scitex-etc

<!-- scitex-badges:start -->
[![PyPI](https://img.shields.io/pypi/v/scitex-etc.svg)](https://pypi.org/project/scitex-etc/)
[![Python](https://img.shields.io/pypi/pyversions/scitex-etc.svg)](https://pypi.org/project/scitex-etc/)
[![Tests](https://github.com/ywatanabe1989/scitex-etc/actions/workflows/test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-etc/actions/workflows/test.yml)
[![Install Test](https://github.com/ywatanabe1989/scitex-etc/actions/workflows/install-test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-etc/actions/workflows/install-test.yml)
[![Coverage](https://codecov.io/gh/ywatanabe1989/scitex-etc/graph/badge.svg)](https://codecov.io/gh/ywatanabe1989/scitex-etc)
[![Docs](https://readthedocs.org/projects/scitex-etc/badge/?version=latest)](https://scitex-etc.readthedocs.io/en/latest/)
[![License: AGPL v3](https://img.shields.io/badge/license-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
<!-- scitex-badges:end -->


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
