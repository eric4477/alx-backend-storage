#!/usr/bin/env python3

""" Redis client module """

import redis
import uuid
from typing import Union, Callable, Optional, Any


class Cache:
    """
    The Cache class provides a simple interface to interact with a Redis
    database. It allows storing data of various types (str, bytes, int,
    float) and retrieves them using randomly generated keys.
    """

    def __init__(self):
        """
        Initialize a new Cache instance.
        This sets up a connection to a Redis database and flushes any
        existing data.
        """
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in the Redis database with a randomly
        generated key.

        :param data: The data to be stored, which can be of type str,
                     bytes, int, or float.
        :return: The randomly generated key as a string.
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str,
            fn: Optional[Callable[[bytes], Any]] = None) -> Any:
        """
        Retrieve data from Redis with the given key and apply an optional
        conversion function.

        :param key: The key to retrieve the data.
        :param fn: An optional callable used to convert the data.
        :return: The data from Redis, optionally transformed by fn.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis with the given key.

        :param key: The key to retrieve the data.
        :return: The data from Redis as a string, or None if the key does
                 not exist.
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis with the given key.

        :param key: The key to retrieve the data.
        :return: The data from Redis as an integer, or None if the key
                 does not exist.
        """
        return self.get(key, lambda x: int(x))
