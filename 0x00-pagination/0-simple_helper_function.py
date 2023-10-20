#!/usr/bin/env python3
"""
Simple helper function

Example 1:
    >>> res = index_range(1, 7)
    >>> print(type(res))
    >>> <class 'tuple'>
    >>> print(res)
    >>> (0, 7)

Example 2:
    >>> res = index_range(page=3, page_size=15)
    >>> print(type(res))
    >>> <class 'tuple'>
    >>> print(res)
    >>> (30, 45)
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    Definition of the function index_range

    The function should return a tuple of size two containing
    a start index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.

    Page numbers are 1-indexed, i.e. the first page is page 1.

    :param page: integer
    :param page_size: integer
    :return: a tuple of start index and end index
    """
    end = page * page_size
    start = end - page_size

    return start, end
