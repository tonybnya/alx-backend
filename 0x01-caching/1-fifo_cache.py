#!/usr/bin/env python3
""" FIFO caching
"""
from base_caching import BaseCaching
from collections import OrderedDict
from typing import Union


class FIFOCache(BaseCaching):
    """FIFOCache inherits from BaseCaching"""

    def __init__(self):
        """Initialize this child class using the parent class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key: str, item: str) -> None:
        """Add an item to the cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            popped_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {popped_key}")

    def get(self, key: str) -> Union[None, str]:
        """Get the value from the cache linked to key"""
        return self.cache_data.get(key, None)
