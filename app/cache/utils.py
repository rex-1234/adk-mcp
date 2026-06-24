from app.cache.redis_client import (
    redis_client
)


async def delete_cache(
    key: str
):

    await redis_client.delete(
        key
    )
