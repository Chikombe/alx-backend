#!/usr/bin/env python3
"""
3-lru_cache.py: This module implements an LRU caching system.
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache: Implements a caching system with LRU eviction policy.
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
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache by key. If the key is None or the key
        does not exist, return None.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The cached item, or None if the key does not exist.
        """
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
