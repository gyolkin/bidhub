from fastapi import FastAPI
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka

from bidhub.main.providers import (
    ConfigurationProvider,
    ConnectionsProvider,
    DatabaseProvider,
    PasswordManagerProvider,
    UseCasesProvider,
    SendingProvider,
    TaskQueueProvider,
    ServicesProvider,
    ValidatorsProvider,
)
from bidhub.presentation.web_api.exception_handlers import setup_exception_handlers
from bidhub.presentation.web_api.config import load_web_config
from bidhub.infrastructure.rabbit_mq.config import load_rabbit_config
from bidhub.infrastructure.redis.config import load_redis_config
from bidhub.infrastructure.sqla_db.config import load_db_config
from bidhub.presentation.web_api.rate_limiter import RateLimiterMiddleware
from bidhub.presentation.web_api.router import router

from .web_api_providers import AuthProvider, RateLimiterProvider


def create_app() -> FastAPI:
    app = FastAPI(
        title='BidHub WebAPI',
        version='0.1.0',
    )
    app.include_router(router)
    setup_exception_handlers(app)
    return app


def create_production_app() -> FastAPI:
    app = create_app()
    container = make_async_container(
        ConfigurationProvider(
            web_config=load_web_config(),
            db_config=load_db_config(),
            rabbit_config=load_rabbit_config(),
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
        AuthProvider(),
        RateLimiterProvider(),
    )
    setup_dishka(container, app)
    app.add_middleware(RateLimiterMiddleware)
    return app
