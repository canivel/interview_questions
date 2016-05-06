# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the
# following operations: get and set.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

import collections

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()


    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.cache:
            return -1

        val = self.cache.pop(key)
        self.cache[key] =  val # set key as the new one
        return val


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """

        if key in self.cache:
            self.cache.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.cache.popitem(last=False)

        self.cache[key] = value