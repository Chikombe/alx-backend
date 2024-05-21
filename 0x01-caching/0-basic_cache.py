#!/usr/bin/env python3
"""
0-basic_cache.py: This module implements a basic caching system.
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    BasicCache: A basic caching system without a size limit.
    """

    def put(self, key, item):
        """
        Add an item to the cache. If the key or item is None, do nothing.
        
        Args:
            key: The key under which the item is stored.
            item: The item to store in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key. If the key is None or the key does not exist, return None.
        
        Args:
            key: The key for the item to retrieve.
        
        Returns:
            The cached item, or None if the key does not exist.
        """
        return self.cache_data.get(key)
