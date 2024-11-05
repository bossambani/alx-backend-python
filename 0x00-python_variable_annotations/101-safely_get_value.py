#!/usr/bin/env python3
"""101-safely_get_value.py"""

from typing import TypeVar, Mapping, Any, Union
T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any,
        default=Union[T, None]) -> Union[Any, T]:
    """TypeVar implementation"""
    if key in dct:
        return dct[key]
    else:
        return default
