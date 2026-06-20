#!/usr/bin/env python3
# File: tests/scitex_etc/test__grid.py
# ----------------------------------------
"""Tests for scitex_etc._grid — combinatorial parameter-grid helpers."""

import os

import pytest


class TestYieldGrids:
    """yield_grids: enumerate every combination of a parameter grid."""

    def test_yield_grids_returns_all_combinations(self):
        # Arrange
        from scitex_etc import yield_grids

        grid = {"a": [1, 2], "b": ["x", "y"]}
        # Act
        result = list(yield_grids(grid))
        # Assert
        assert result == [
            {"a": 1, "b": "x"},
            {"a": 1, "b": "y"},
            {"a": 2, "b": "x"},
            {"a": 2, "b": "y"},
        ]

    def test_yield_grids_random_preserves_combination_set(self):
        # Arrange
        from scitex_etc import yield_grids

        grid = {"a": [1, 2], "b": ["x", "y"]}
        # Act
        shuffled = list(yield_grids(grid, random=True))
        # Assert
        assert sorted(map(repr, shuffled)) == sorted(map(repr, yield_grids(grid)))


class TestCountGrids:
    """count_grids: total number of combinations in a grid."""

    def test_count_grids_returns_product_of_lengths(self):
        # Arrange
        from scitex_etc import count_grids

        grid = {"a": [1, 2, 3], "b": ["x", "y"]}
        # Act
        total = count_grids(grid)
        # Assert
        assert total == 6


if __name__ == "__main__":
    pytest.main([os.path.abspath(__file__)])
