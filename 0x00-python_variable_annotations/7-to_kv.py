#!/usr/bin/env python3
"""
type-annotated function to_kv that takes a string k and
an int OR float v as arguments and returns a tuple. The
first element of the tuple is the string k. The second
element is the square of the int/float v and should be
annotated as a float.
"""
from typing import Tuple, Union, List


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string `k` and a list `v` of integers or floats,
    and returns a tuple with the string and the square of the sum of `v`.
    Args:
        k (str): A string key.
        v (List[Union[int, float]]): A list of integers or floats.

    Returns:
        Tuple[str, float]: A tuple containing the string `k` and
        the square of the sum of elements in `v`.
    """
    square = v**2

    return k, square
