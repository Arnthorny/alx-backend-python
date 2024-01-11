#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return values with the appropriate
types
"""
from typing import Tuple, Sequence, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotated function
    """
    return [(i, len(i)) for i in lst]
