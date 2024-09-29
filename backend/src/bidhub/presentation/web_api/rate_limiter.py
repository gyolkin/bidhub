from fastapi.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware

from bidhub.infrastructure.redis.rate_limiter import RedisRateLimiter


class RateLimiterMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        async with request.app.state.dishka_container() as container:
            rate_limiter: RedisRateLimiter = await container.get(RedisRateLimiter)
        await rate_limiter.check_key(request.client.host)
        response = await call_next(request)
        return response
