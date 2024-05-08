#!/usr/bin/env python3
""" BaseCaching module with LIFO
"""
from base_caching import BaseCaching


class LIFOCache (BaseCaching):
    """
    implement class
    """
    def __init__(self):
        """ constructor method"""
        super().__init__()

    def put(self, key, item):
        """ add item to caching && handle lifo"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            key_removed, _ = self.cache_data.popitem()
            print("DISCARD: {}".format(key_removed))
        self.cache_data[key] = item

    def get(self, key):
        """ get item from the caching storage"""
        if key is None:
            return None
        else:
            return self.cache_data.get(key, None)
