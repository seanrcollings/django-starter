from typing import List, Union, Sized, Any


def safe_unpack(iterable: Sized, expected_length: int, fill: Any = None):
    """Safely unpack an iterable into a series of arguements.
    If the iterable has fewer element than expected, will be
    filled with a default value

    :param iterable: iterable to unpack, must implemnt __len__
    :param expected_length: expected length of the iterable, number of items being unpacked
    :param fill: value to fill any extra space with, defaults to None
    """
    fill_list = [fill] * (expected_length - len(iterable))
    return (*iterable, *fill_list)  # type: ignore
