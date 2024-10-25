#!/usr/bin/env python3
from typing import List
"""
This module contains a type-annotated function `sum_list`
which takes a list of floats as an argument and returns
their sum as a float.
"""


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): A list of float numbers to be summed.

    Returns:
        float: The sum of all numbers in the input_list.
    """
    initial: float = 0
    for value in input_list:
        initial = initial + value

    return initial
