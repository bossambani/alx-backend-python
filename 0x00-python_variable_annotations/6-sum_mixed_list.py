#!/usr/bin/env python3
"""
This module contains a type-annotated function `sum_mixed_list`
which takes a list of floats and int as arguments and returns
their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of  ints and floats.

    Args:
        mxd_list (List[Union[int,float]]): A list of ints and float numbers to be summed.

    Returns:
        float: The sum of all numbers in the mxd_list.
    """
    total: float = 0

    for value in mxd_lst:
        total += value

    return total
