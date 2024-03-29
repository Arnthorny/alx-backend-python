#!/usr/bin/env python3
"""
Given the parameters and the return values, add type annotations to the
function.

Hint: look into TypeVar
"""
from typing import Union, TypeVar, Any, Mapping

gen_t = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[gen_t, None] =
                     None) -> Union[Any, gen_t]:
    """
    Annotation for function
    """
    if key in dct:
        return dct[key]
    else:
        return default
