#!/usr/bin/env python3
"""
This module contains a function to create a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a given float by a specified multiplier.
    Args:
        multiplier (float): The number to multiply by.
    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of that float and the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplies the input value by the multiplier.
        Args:
            value (float): The float to be multiplied.
        Returns:
            float: The product of the input value and the multiplier.
        """
        return value * multiplier
    return multiplier_function
