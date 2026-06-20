#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: /home/ywatanabe/proj/scitex-etc/tests/conftest.py

"""Anchors pytest rootdir at the project root so the installed
`scitex_etc` package (under ``src/scitex_etc``) resolves correctly
instead of being shadowed by the empty ``tests/scitex_etc/__init__.py``
PS201 mirror parent.

Also wires module-import-time coverage for child Python interpreters
(`subprocess.run([sys.executable, ...])`, demo smoke tests, notebook
executions). `os.environ.setdefault` would be a silent no-op here
because pytest-cov has already set COVERAGE_FILE to a tmp dir by the
time conftest is loaded — must force-set.
"""

from __future__ import annotations

import os
import sysconfig
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent

os.environ["COVERAGE_PROCESS_START"] = str(_PROJECT_ROOT / "pyproject.toml")
os.environ["COVERAGE_FILE"] = str(_PROJECT_ROOT / ".coverage")


def _ensure_subprocess_coverage_shim() -> None:
    """Drop an idempotent `.pth` file in site-packages that auto-starts
    coverage in every child Python interpreter via
    `coverage.process_startup()`.
    """
    purelib = Path(sysconfig.get_paths()["purelib"])
    pth = purelib / "_scitex_etc_subprocess_coverage.pth"
    shim = (
        "import os, coverage\n"
        "if os.environ.get('COVERAGE_PROCESS_START'):\n"
        "    coverage.process_startup()\n"
    )
    try:
        if not pth.exists() or pth.read_text() != shim:
            pth.write_text(shim)
    except OSError:
        # site-packages may be read-only — silently skip.
        pass


_ensure_subprocess_coverage_shim()
