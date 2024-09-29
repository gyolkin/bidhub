from dishka import Provider, Scope, provide, from_context
from redis.asyncio import Redis
from fastapi import Request

from bidhub.presentation.web_api.config import WebConfig
from bidhub.presentation.web_api.constants import JWT_COOKIE_NAME
from bidhub.infrastructure.redis.rate_limiter import RedisRateLimiter
from bidhub.infrastructure.auth.jwt import JwtProcessor, TokenUserIdentityProvider
from bidhub.application.protocols.security import IUserIdentity
from bidhub.application.protocols.persistence import IUserGateway


class AuthProvider(Provider):
    request = from_context(provides=Request, scope=Scope.REQUEST)

    @provide(scope=Scope.APP)
    def jwt_processor(self, web_config: WebConfig) -> JwtProcessor:
        return JwtProcessor(secret=web_config.jwt_secret)

    @provide(scope=Scope.REQUEST)
    def token_identity_provider(
        self,
        request: Request,
        user_gateway: IUserGateway,
        jwt_processor: JwtProcessor,
    ) -> IUserIdentity:
        return TokenUserIdentityProvider(
            user_gateway=user_gateway,
            token_processor=jwt_processor,
            token=request.cookies.get(JWT_COOKIE_NAME),
        )


class RateLimiterProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def rate_limiter(self, redis: Redis) -> RedisRateLimiter:
        return RedisRateLimiter(redis=redis)
