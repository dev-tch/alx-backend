#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache (BaseCaching):
    def __init__(self):
        """ constructor method"""
        super().__init__()

    def put(self, key, item):
        """ add data to caching storage"""
        valid_data = all((key is not None, item is not None))
        if valid_data:
            self.cache_data.update({key: item})

    def get(self, key):
        """ get data from caching storage """
        return self.cache_data.get(key, None)
