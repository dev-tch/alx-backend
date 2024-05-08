#!/usr/bin/env python3
""" BaseCaching module with FIFO
"""
from base_caching import BaseCaching


class FIFOCache (BaseCaching):
    """
    implement class
    """
    def __init__(self):
        """ constructor method"""
        super().__init__()

    def put(self, key, item):
        """ add data to caching storage"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            iterator = iter(self.cache_data)
            key_to_remove = next(iterator)
            del self.cache_data[key_to_remove]
            print("DISCARD: {}".format(key_to_remove))
        self.cache_data[key] = item

    def get(self, key):
        """ get item from the caching storage"""
        if key is None:
            return None
        else:
            return self.cache_data.get(key, None)
