#!/usr/bin/env python3
"""
This module contains a type-annotated function `sum_mixed_list`
which takes a list of floats and int as arguments and returns
their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    total: float = 0

    for value in mxd_lst:
        total += value

    return total
