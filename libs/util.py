from typing import Sized, Any
from django.http import JsonResponse


def safe_unpack(iterable: Sized, expected_length: int, fill: Any = None):
    """Safely unpack an iterable into a series of arguements.
    If the iterable has fewer element than expected, will be
    filled with a default value

    :param iterable: iterable to unpack
    :param expected_length: expected length of the iterable, number of items being unpacked
    :param fill: value to fill any extra space with, defaults to None
    """
    if len(iterable) > expected_length:
        raise ValueError(
            f"Iterable has more than the expected {expected_length} values"
        )
    fill_list = [fill] * (expected_length - len(iterable))
    return (*iterable, *fill_list)  # type: ignore


def error(errors, status=400):
    return JsonResponse({"errors": errors}, status=status)
