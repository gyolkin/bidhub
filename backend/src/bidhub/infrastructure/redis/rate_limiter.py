import time

from redis.asyncio import Redis

from bidhub.infrastructure.exceptions import InfrastructureError


LIMIT_REQUESTS = 40
LIMIT_WINDOW = 60
LIMIT_EXCEED_ERROR = 'You send requests too frequently. Please try again later.'


class RateLimiterError(InfrastructureError):
    pass


class RedisRateLimiter:
    def __init__(self, redis: Redis):
        self.redis = redis

    async def check_key(self, identifier: str) -> None:
        key = self._create_key(identifier)
        async with self.redis.pipeline(transaction=True) as pipe:
            await pipe.incr(key)
            await pipe.expire(key, LIMIT_WINDOW)
            results = await pipe.execute()
            request_count = results[0]
            if request_count > LIMIT_REQUESTS:
                raise RateLimiterError(LIMIT_EXCEED_ERROR)

    def _create_key(self, identifier: str) -> str:
        return f'{identifier}:{time.time() // LIMIT_WINDOW}'
