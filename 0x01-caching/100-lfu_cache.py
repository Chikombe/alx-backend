#!/usr/bin/env python3
"""
100-lfu_cache.py: This module implements an LFU caching system.
"""

from collections import defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.freq = defaultdict(int)
        self.use_order = {}
        self.time = 0

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        
        self.time += 1
        
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.use_order[key] = self.time
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                self.evict()
            self.cache_data[key] = item
            self.freq[key] = 1
            self.use_order[key] = self.time

    def get(self, key):
        """Retrieve an item by key"""
        if key is None or key not in self.cache_data:
            return None
        
        self.time += 1
        self.freq[key] += 1
        self.use_order[key] = self.time
        return self.cache_data[key]

    def evict(self):
        """Evict the least frequently used item"""
        min_freq = min(self.freq.values())
        lfu_keys = [k for k, v in self.freq.items() if v == min_freq]
        if len(lfu_keys) == 1:
            lfu_key = lfu_keys[0]
        else:
            lfu_key = min(lfu_keys, key=lambda k: self.use_order[k])
        
        del self.cache_data[lfu_key]
        del self.freq[lfu_key]
        del self.use_order[lfu_key]
        print(f"DISCARD: {lfu_key}")
