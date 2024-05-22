#!/usr/bin/env python3
"""
100-lfu_cache.py: This module implements an LFU caching system.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache: Implements a caching system with LFU eviction policy.
    """

    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.freq = {}
        self.use_order = {}

    def put(self, key, item):
        """
        Add an item to the cache. If the key or item is None, do nothing.

        Args:
            key: The key under which the item is stored.
            item: The item to store in the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.freq[key] += 1
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    self.evict()
                self.cache_data[key] = item
                self.freq[key] = 1
                self.use_order[key] = len(self.use_order)
            self.cache_data[key] = item
            self.update_use_order(key)

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
            self.freq[key] += 1
            self.update_use_order(key)
            return self.cache_data[key]
        return None
