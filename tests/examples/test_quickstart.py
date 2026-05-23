#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: /home/ywatanabe/proj/scitex-etc/tests/examples/test_quickstart.py

"""Smoke test for examples/quickstart.py.

Per scitex-dev audit-project PS303: every example must have a matching
test under tests/examples/. Runs the example end-to-end (it prints the
public API and returns 0 without blocking) and verifies it exits clean.
"""

import subprocess
import sys
from pathlib import Path

EXAMPLE = Path(__file__).resolve().parents[2] / "examples" / "quickstart.py"


def test_quickstart_example_file_exists_on_disk():
    # Arrange
    example = EXAMPLE
    # Act
    present = example.exists()
    # Assert
    assert present, f"missing example: {example}"


def test_quickstart_example_runs_and_exits_zero():
    # Arrange
    cmd = [sys.executable, str(EXAMPLE)]
    # Act
    result = subprocess.run(cmd, capture_output=True, text=True)
    # Assert
    assert result.returncode == 0, result.stderr
