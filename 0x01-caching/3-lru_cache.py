#!/usr/bin/env python3
""" BaseCaching module with LRU
"""
from base_caching import BaseCaching
from collections import deque


class LRUCache (BaseCaching):
    """
    implement class
    """
    def __init__(self):
        """ constructor method"""
        super().__init__()
        self.deque_container = deque()

    def put(self, key, item):
        """ add item to caching && handle lifo"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            # here we move the key to end (most used )
            self.deque_container.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                old_key = self.deque_container.popleft()
                del self.cache_data[old_key]
                print("DISCARD: {}".format(old_key))
        self.cache_data[key] = item
        self.deque_container.append(key)

    def get(self, key):
        """ get item from the caching storage"""
        if (key is None) or (key not in self.cache_data):
            return None
        self.deque_container.remove(key)
        self.deque_container.append(key)
        return self.cache_data.get(key, None)
