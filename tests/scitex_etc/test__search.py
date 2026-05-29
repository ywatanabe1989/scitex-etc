#!/usr/bin/env python3
# File: tests/scitex_etc/test__search.py
# ----------------------------------------
"""Tests for scitex_etc._search — regex pattern search over strings."""

import os

import pytest


class TestSearch:
    """search: locate regex matches within a list of strings."""

    def test_search_finds_single_regex_match(self):
        # Arrange
        from scitex_etc import search

        strings = ["apple", "orange", "banana"]
        # Act
        indices, matched = search("orange", strings)
        # Assert
        assert (indices, matched) == ([1], ["orange"])

    def test_search_matches_multiple_substring_occurrences(self):
        # Arrange
        from scitex_etc import search

        strings = ["apple", "orange", "apple_juice", "orange_juice"]
        # Act
        indices, matched = search("orange", strings)
        # Assert
        assert matched == ["orange", "orange_juice"]

    def test_search_only_perfect_match_excludes_partial(self):
        # Arrange
        from scitex_etc import search

        strings = ["orange", "orange_juice"]
        # Act
        indices, matched = search("orange", strings, only_perfect_match=True)
        # Assert
        assert matched == ["orange"]


if __name__ == "__main__":
    pytest.main([os.path.abspath(__file__)])
