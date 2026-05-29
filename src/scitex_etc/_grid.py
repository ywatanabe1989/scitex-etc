#!/usr/bin/env python3
# File: src/scitex_etc/_grid.py

"""Combinatorial parameter-grid iteration helpers.

Generic utilities for parameter sweeps: count the number of combinations in a
grid and yield each combination as a dict. No domain ties — pure stdlib.
"""

from __future__ import annotations

import itertools as _itertools
import random as _random


def yield_grids(params_grid: dict, random: bool = False):
    """Yield every parameter combination from a grid as a dict.

    Parameters
    ----------
    params_grid : dict
        Mapping of parameter name -> list of candidate values.
    random : bool, optional
        If True, yield the combinations in shuffled order (default False).

    Yields
    ------
    dict
        One combination, mapping each parameter name to a single value.

    Example
    -------
    >>> grid = {"a": [1, 2], "b": ["x", "y"]}
    >>> list(yield_grids(grid))
    [{'a': 1, 'b': 'x'}, {'a': 1, 'b': 'y'}, {'a': 2, 'b': 'x'}, {'a': 2, 'b': 'y'}]
    """
    combinations = list(_itertools.product(*params_grid.values()))
    if random:
        _random.shuffle(combinations)
    for values in combinations:
        yield dict(zip(params_grid.keys(), values))


def count_grids(params_grid: dict) -> int:
    """Return the total number of combinations in a parameter grid.

    Parameters
    ----------
    params_grid : dict
        Mapping of parameter name -> list of candidate values.

    Returns
    -------
    int
        Product of the lengths of all value lists.
    """
    num_combinations = 1
    for values in params_grid.values():
        num_combinations *= len(values)
    return num_combinations


# EOF
