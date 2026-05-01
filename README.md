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

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Interactive keyboard input utilities for the SciTeX ecosystem.</b></p>

<p align="center">
  <a href="https://scitex-etc.readthedocs.io/">Full Documentation</a> · <code>pip install scitex-etc</code>
</p>

---

## Problem and Solution

| # | Problem | Solution |
|---|---------|----------|
| 1 | **Scripts that pause for a keypress need raw-stdin + termios gymnastics** — 15 lines of OS-dependent boilerplate | **`wait_key()` / `count()`** — one import; handles Linux/macOS/Windows; falls back cleanly when stdin isn't a TTY |

## Installation

```bash
pip install scitex-etc
```

## Quick Start

```python
from scitex_etc import wait_key, count

key = wait_key()  # Wait for a single keypress
count(5)          # Countdown timer
```

## 1 Interfaces

<details>
<summary><strong>Python API</strong></summary>

<br>

```python
from scitex_etc import wait_key, count

# Block until a single key is pressed; returns the key as a string.
key = wait_key()

# Countdown helper — prints "5… 4… 3…" and waits a second between each.
count(5)
```

</details>

## Part of SciTeX

`scitex-etc` is part of [**SciTeX**](https://scitex.ai). Install via
the umbrella with `pip install scitex[etc]` to use as
`scitex.etc` (Python) or `scitex etc ...` (CLI).

>Four Freedoms for Research
>
>0. The freedom to **run** your research anywhere — your machine, your terms.
>1. The freedom to **study** how every step works — from raw data to final manuscript.
>2. The freedom to **redistribute** your workflows, not just your papers.
>3. The freedom to **modify** any module and share improvements with the community.
>
>AGPL-3.0 — because we believe research infrastructure deserves the same freedoms as the software it runs on.

## License

AGPL-3.0

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
</p>
