from fastapi import FastAPI
from fastapi.responses import JSONResponse

from bidhub.infrastructure.redis.rate_limiter import RateLimiterError
from bidhub.infrastructure.exceptions import InfrastructureError
from bidhub.application.exceptions.base import ApplicationError
from bidhub.core.exceptions.base import CoreError


def setup_exception_handlers(app: FastAPI) -> None:
    app.exception_handler(CoreError)(_core_error_handler)
    app.exception_handler(ApplicationError)(_application_error_handler)
    app.exception_handler(RateLimiterError)(_rate_limiter_error_handler)
    app.exception_handler(InfrastructureError)(_infrastructure_error_handler)


async def _core_error_handler(_, error: ApplicationError) -> JSONResponse:
    return JSONResponse(content={'message': str(error)}, status_code=400)


async def _application_error_handler(_, error: ApplicationError) -> JSONResponse:
    return JSONResponse(content={'message': str(error)}, status_code=400)


async def _rate_limiter_error_handler(_, error: RateLimiterError) -> JSONResponse:
    return JSONResponse(content={'message': str(error)}, status_code=419)


async def _infrastructure_error_handler(_, error: InfrastructureError) -> JSONResponse:
    return JSONResponse(content={'message': str(error)}, status_code=400)
