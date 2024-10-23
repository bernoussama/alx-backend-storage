#!/usr/bin/env python3
"""
exercise
"""
from typing import Callable, Union
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
        self._redis.flushdb(True)

    def store(self, data: Union[bytes, str, int, float]) -> str:
        """
        Store data in the cache
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(
        self,
        key: str,
        fn: Callable = None,
    ) -> Union[str, bytes, int, float]:
        """Retrieves a value from Redis Cache"""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """Retrieves a string value from a Redis cache"""
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieves an integer value from a Redis cache."""
        return self.get(key, lambda x: int(x))
