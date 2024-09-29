from dishka import Provider, Scope, provide

from bidhub.presentation.web_api.config import WebConfig
from bidhub.infrastructure.redis.config import RedisConfig
from bidhub.infrastructure.rabbit_mq.config import RabbitConfig
from bidhub.infrastructure.sqla_db.config import DatabaseConfig


class ConfigurationProvider(Provider):
    def __init__(
        self,
        *,
        web_config: WebConfig,
        redis_config: RedisConfig,
        rabbit_config: RabbitConfig,
        db_config: DatabaseConfig,
    ) -> None:
        super().__init__()
        self._web_config = web_config
        self._redis_config = redis_config
        self._rabbit_config = rabbit_config
        self._db_config = db_config

    @provide(scope=Scope.APP)
    def web_config(self) -> WebConfig:
        return self._web_config

    @provide(scope=Scope.APP)
    def redis_config(self) -> RedisConfig:
        return self._redis_config

    @provide(scope=Scope.APP)
    def rabbit_config(self) -> RabbitConfig:
        return self._rabbit_config

    @provide(scope=Scope.APP)
    def db_config(self) -> DatabaseConfig:
        return self._db_config
