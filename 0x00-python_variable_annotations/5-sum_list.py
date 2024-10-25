#!/usr/bin/env python3
from typing import List
"""
type-annotated function sum_list which takes a list
input_list of floats as argument and returns their
sum as a float.
"""


def sum_list(input_list: List[float]) -> float:
    initial: float = 0
    for value in input_list:
        initial = initial + value

    return initial
