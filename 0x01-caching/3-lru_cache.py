#!/usr/bin/env python3
""" Least Recently Used caching module.
"""
from base_caching import BaseCaching
from collections import OrderedDict
from typing import Union


class LRUCache(BaseCaching):
    """LRUCache inherits from BaseCaching"""

    def __init__(self):
        """Initialize this child class from the parent class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key: str, item: str) -> None:
        """Add an item to the cache"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                popped_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {popped_key}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key: str) -> Union[None, str]:
        """Get the value from the cache linked to key"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)

        return self.cache_data.get(key, None)
