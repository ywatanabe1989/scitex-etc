#!/usr/bin/env python3
# File: src/scitex_etc/_search.py

"""Regex pattern search over collections of strings.

Generic cross-cutting helper. Stdlib-only at runtime: numpy, pandas, xarray and
natsort are all *optional* — when present, their array/series types are accepted
as inputs and natural sort ordering is used; otherwise plain lists and the
builtin ``sorted`` are used.
"""

from __future__ import annotations

import re
from collections import abc

try:  # optional — natural sort ordering when available
    from natsort import natsorted as _natsorted
except ImportError:  # pragma: no cover — fallback path

    def _natsorted(iterable):
        return sorted(iterable)


def _to_list(string_or_pattern):
    """Coerce assorted string containers into a plain list of strings."""
    # numpy arrays (optional dependency)
    try:
        import numpy as _np

        if isinstance(string_or_pattern, _np.ndarray):
            return string_or_pattern.tolist()
    except ImportError:
        pass

    # pandas Series / Index (optional dependency)
    try:
        import pandas as _pd

        if isinstance(string_or_pattern, (_pd.Series, _pd.Index)):
            return string_or_pattern.tolist()
    except ImportError:
        pass

    # xarray DataArray (optional, lazy to avoid atexit hang issues)
    try:
        import xarray as _xr

        if isinstance(string_or_pattern, _xr.DataArray):
            return string_or_pattern.tolist()
    except ImportError:
        pass

    if isinstance(string_or_pattern, abc.KeysView):
        return list(string_or_pattern)
    if not isinstance(string_or_pattern, (list, tuple)):
        return [string_or_pattern]
    return string_or_pattern


def search(
    patterns,
    strings,
    only_perfect_match: bool = False,
    as_bool: bool = False,
    ensure_one: bool = False,
):
    """Search for patterns in strings using regular expressions.

    Parameters
    ----------
    patterns : str or list of str
        The pattern(s) to search for. A single string or a list of strings.
    strings : str or list of str
        The string(s) to search in. A single string or a list of strings.
    only_perfect_match : bool, optional
        If True, only exact matches are considered (default False).
    as_bool : bool, optional
        If True, return a boolean mask instead of indices (default False).
    ensure_one : bool, optional
        If True, assert exactly one match is found (default False).

    Returns
    -------
    tuple
        - If ``as_bool`` is False: ``(indices, matched_strings)`` where
          ``indices`` is a list of int positions of matches.
        - If ``as_bool`` is True: ``(mask, matched_strings)`` where ``mask`` is
          a boolean sequence (numpy array when numpy is installed, else a list)
          flagging matched positions.

    Example
    -------
    >>> patterns = ['orange', 'banana']
    >>> strings = ['apple', 'orange', 'apple', 'apple_juice', 'banana', 'orange_juice']
    >>> search(patterns, strings)
    ([1, 4, 5], ['orange', 'banana', 'orange_juice'])

    >>> search('orange', strings)
    ([1, 5], ['orange', 'orange_juice'])
    """
    patterns = _to_list(patterns)
    strings = _to_list(strings)

    indices_matched = []
    for pattern in patterns:
        for index_str, string in enumerate(strings):
            if only_perfect_match:
                if pattern == string:
                    indices_matched.append(index_str)
            else:
                if re.search(pattern, string):
                    indices_matched.append(index_str)

    indices_matched = _natsorted(indices_matched)
    keys_matched = [strings[index] for index in indices_matched]

    if ensure_one:
        assert len(indices_matched) == 1, (
            f"Expected exactly one match, but found {len(indices_matched)}"
        )

    if as_bool:
        unique_indices = sorted(set(indices_matched))
        try:
            import numpy as _np

            bool_matched = _np.zeros(len(strings), dtype=bool)
            bool_matched[unique_indices] = True
        except ImportError:
            bool_matched = [False] * len(strings)
            for index in unique_indices:
                bool_matched[index] = True
        return bool_matched, keys_matched

    return indices_matched, keys_matched


# EOF
