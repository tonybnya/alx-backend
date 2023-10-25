#!/usr/bin/env python3
""" Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inherist from BaseCaching
    - implements a 'put' method
    - implements a 'get' method
    """

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        self.cache_data.update({key: item})

    def get(self, key):
        """Get the value from the cache linked to key"""
        self.cache_data.get(key, None)