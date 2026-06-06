---
description: |
  [TOPIC] scitex-etc Installation
  [DETAILS] pip install scitex-etc; pure Python; smoke verify with import + count_grids/search/media.
tags: [scitex-etc-installation]
---

# Installation

## Standard

```bash
pip install scitex-etc
```

Pure-Python; no required runtime dependencies.

## Verify

```bash
python -c "import scitex_etc; print(scitex_etc.__version__)"
python -c "from scitex_etc import count_grids, yield_grids, search; print('ok')"
python -c "from scitex_etc.media import render; print('ok')"
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
