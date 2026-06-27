#!/usr/bin/env python3

def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if function_to_apply is None:
        return None
    iter(iterable)
    def generator():
        for item in iterable:
            yield function_to_apply(item)
    return generator()