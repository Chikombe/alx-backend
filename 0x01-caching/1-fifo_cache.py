#!/usr/bin/env python3
"""
1-fifo_cache.py: This module implements a FIFO caching system.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache: Implements a caching system with FIFO eviction policy.
    """

    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache. If the key or item is None, do nothing.

        Args:
            key: The key under which the item is stored.
            item: The item to store in the cache.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    oldest_key = self.order.pop(0)
                    del self.cache_data[oldest_key]
                    print(f"DISCARD: {oldest_key}")
            self.cache_data[key] = item
            self.order.append(key)

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
