from faststream import FastStream
from faststream.rabbit import RabbitBroker
from dishka import make_async_container
from dishka.integrations.faststream import setup_dishka

from bidhub.main.providers import (
    ConfigurationProvider,
    ConnectionsProvider,
    DatabaseProvider,
    ServicesProvider,
    PasswordManagerProvider,
    UseCasesProvider,
    SendingProvider,
    TaskQueueProvider,
    ValidatorsProvider,
)
from bidhub.presentation.web_api.config import load_web_config
from bidhub.infrastructure.rabbit_mq.config import load_rabbit_config
from bidhub.infrastructure.redis.config import load_redis_config
from bidhub.infrastructure.sqla_db.config import load_db_config
from bidhub.presentation.worker.router import router


def create_worker() -> FastStream:
    rabbit_config = load_rabbit_config()
    broker = RabbitBroker(url=rabbit_config.uri)
    broker.include_router(router)
    app = FastStream(broker)

    container = make_async_container(
        ConfigurationProvider(
            web_config=load_web_config(),
            db_config=load_db_config(),
            rabbit_config=rabbit_config,
            redis_config=load_redis_config(),
        ),
        ConnectionsProvider(),
        DatabaseProvider(),
        ValidatorsProvider(),
        PasswordManagerProvider(),
        SendingProvider(),
        TaskQueueProvider(),
        ServicesProvider(),
        UseCasesProvider(),
    )
    setup_dishka(container, app)
    return app
