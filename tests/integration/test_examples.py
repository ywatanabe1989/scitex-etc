"""Smoke tests: every example script must run to completion."""

import subprocess
import sys
from pathlib import Path

import pytest

EXAMPLES = sorted(Path(__file__).resolve().parents[2].joinpath("examples").glob("*.py"))


def test_examples_directory_contains_scripts():
    # Arrange
    examples = EXAMPLES
    # Act
    count = len(examples)
    # Assert
    assert count > 0, "no example scripts found"


@pytest.mark.parametrize("example", EXAMPLES, ids=lambda p: p.name)
def test_example_script_runs_and_exits_zero(example, tmp_path):
    # Arrange
    cmd = [sys.executable, str(example)]
    # Act
    result = subprocess.run(
        cmd, cwd=tmp_path, capture_output=True, text=True, timeout=120
    )
    # Assert
    assert result.returncode == 0, f"{example.name} failed: {result.stderr}"
