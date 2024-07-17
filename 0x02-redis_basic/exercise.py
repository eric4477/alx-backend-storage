#!/usr/bin/env python3

""" Redis client module """

import redis
import uuid
from typing import Union


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
