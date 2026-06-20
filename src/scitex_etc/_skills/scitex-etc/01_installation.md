---
description: |
  [TOPIC] scitex-etc Installation
  [DETAILS] pip install scitex-etc; pure Python, no extras; smoke verify with import + wait_key.
tags: [scitex-etc-installation]
---

# Installation

## Standard

```bash
pip install scitex-etc
```

Pure-Python; no required runtime dependencies. Uses stdlib termios on
POSIX and msvcrt on Windows for getch-style keypress reading.

## Verify

```bash
python -c "import scitex_etc; print(scitex_etc.__version__)"
python -c "from scitex_etc import wait_key, count; print('ok')"
```

## Editable install (development)

```bash
git clone https://github.com/ywatanabe1989/scitex-etc
cd scitex-etc
pip install -e '.[dev]'
```

## Umbrella alternative

```bash
pip install scitex   # exposes scitex.etc as a submodule
```

See SKILL.md for the standalone-vs-umbrella import rule.
