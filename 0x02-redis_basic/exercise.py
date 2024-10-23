#!/usr/bin/env python3
"""
exercise
"""
from typing import Union
import redis
import uuid


class Cache:
    """
    class representing a cache
    """

    def __init__(self):
        """
        initialize the cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, str, int, float]) -> str:
        """
        Store data in the cache
        """
        random_key = uuid.uuid4()
        self._redis.set(random_key, data)
        return f"{random_key}"
