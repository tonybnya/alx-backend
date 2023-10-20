#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
from math import ceil
from typing import Any, Dict, List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the range of the dataset
        """
        # Use assert to verify if both arguments are integers greater than 0
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        # Get the start and end indexes to paginate the dataset
        start, end = index_range(page, page_size)

        # Get the dataset
        dataset = self.dataset()
        n = len(dataset)

        # Check if pages are out of range
        if start > n:
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Get info of some pages
        """
        # Set an empty dict
        pages = {}

        # Get the entire dataset
        dataset = self.dataset()
        n = len(dataset)

        # Get the dataset to paginate
        data = self.get_page(page, page_size)
        size = len(data)

        # Set some values of the dict
        next_page = page + 1 if size > 0 else None
        prev_page = page - 1 if page > 1 else None
        total_pages = round(n / size) if size > 0 else ceil(n / page_size)

        # Update the dict
        pages.update({
            'page_size': size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        })

        return pages
