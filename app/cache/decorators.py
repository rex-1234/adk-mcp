import json
from functools import wraps

from app.cache.redis_client import (
    redis_client
)


def cached(prefix: str, ttl: int = 3600):
    """
    Generic Redis cache decorator
    """

    def decorator(func):

        @wraps(func)
        async def wrapper(
            filename: str
        ):

            cache_key = f"{prefix}:{filename}"

            # check cache

            cached_data = await redis_client.get(
                cache_key
            )

            if cached_data:

                print(
                    f"CACHE HIT: {cache_key}"
                )

                return cached_data

            print(
                f"CACHE MISS: {cache_key}"
            )

            # execute function

            result = await func(
                filename
            )

            # store in redis

            await redis_client.set(
                cache_key,
                result,
                ex=ttl
            )

            return result

        return wrapper

    return decorator
