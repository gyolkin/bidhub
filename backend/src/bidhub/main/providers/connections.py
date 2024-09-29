from typing import AsyncIterable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)
from aio_pika import connect_robust
from aio_pika.abc import AbstractChannel as IRabbitChannel
from redis.asyncio import Redis as Redis

from bidhub.infrastructure.redis.config import RedisConfig
from bidhub.infrastructure.sqla_db.config import DatabaseConfig
from bidhub.infrastructure.rabbit_mq.config import RabbitConfig
from bidhub.infrastructure.sqla_db.models import metadata_obj  # noqa


class ConnectionsProvider(Provider):
    @provide(scope=Scope.APP)
    def sqlalchemy_engine(self, db_config: DatabaseConfig) -> AsyncEngine:
        return create_async_engine(db_config.uri, echo=True)

    @provide(scope=Scope.APP)
    def sqlalchemy_sessionmaker(
        self,
        engine: AsyncEngine,
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(
            bind=engine,
            autoflush=False,
            expire_on_commit=False,
            class_=AsyncSession,
        )

    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def sqlalchemy_session(
        self,
        sessionmaker: async_sessionmaker[AsyncSession],
    ) -> AsyncIterable[AsyncSession]:
        async with sessionmaker() as session:
            yield session

    @provide(scope=Scope.APP)
    async def rabbit_channel(self, rabbit_config: RabbitConfig) -> IRabbitChannel:
        connection = await connect_robust(rabbit_config.uri)
        return await connection.channel()

    @provide(scope=Scope.APP)
    async def redis(self, redis_config: RedisConfig) -> Redis:
        redis = await Redis.from_url(url=redis_config.uri, decode_responses=True)
        return redis
