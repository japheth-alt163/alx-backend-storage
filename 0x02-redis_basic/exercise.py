#!/usr/bin/env python3

"""
Cache module
"""

import redis
import uuid
from functools import wraps
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        count_key = key + ":count"
        self._redis.incr(count_key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        inputs_key = key + ":inputs"
        outputs_key = key + ":outputs"
        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))
        return result
    return wrapper


class Cache:
    """
    Cache class for storing data in Redis.
    """

    def __init__(self) -> None:
        """
        Initialize Cache instance and flush the Redis database.
        """
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a random key and return the key.

        Args:
            data (Union[str, bytes, int, float]): Data to store in the cache.

        Returns:
            str: The randomly generated key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def replay(self, method: Callable) -> None:
        """
        Display the history of calls for a particular method.

        Args:
            method (Callable): The method to display the history for.
        """
        key = method.__qualname__
        inputs_key = key + ":inputs"
        outputs_key = key + ":outputs"
        inputs = self._redis.lrange(inputs_key, 0, -1)
        outputs = self._redis.lrange(outputs_key, 0, -1)
        num_calls = self._redis.get(key + ":count") or 0
        print(f"{key} was called {num_calls.decode()} times:")
        for args, result in zip(inputs, outputs):
            print(f"{key}{args.decode()} -> {result.decode()}")


if __name__ == "__main__":
    cache = Cache()

    cache.store("foo")
    cache.store("bar")
    cache.store(42)

    cache.replay(cache.store)
