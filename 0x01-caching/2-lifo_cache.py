#!/usr/bin/env python3
"""
2-lifo_cache.py: This module implements a LIFO caching system.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache: Implements a caching system with LIFO eviction policy.
    """

    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Add an item to the cache. If the key or item is None, do nothing.

        Args:
            key: The key under which the item is stored.
            item: The item to store in the cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS and
                    key not in self.cache_data:
                if self.last_key is not None:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        If the key is None or the key does not exist, return None.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The cached item, or None if the key does not exist.
        """
        return self.cache_data.get(key)
