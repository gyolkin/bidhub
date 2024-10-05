from fastapi import Response

from dishka.integrations.fastapi import FromDishka, inject

from bidhub.presentation.web_api.constants import JWT_COOKIE_NAME, JWT_COOKIE_LIFETIME
from bidhub.infrastructure.auth.jwt import JwtProcessor
from bidhub.application.dto.user import AuthenticateUserRequest
from bidhub.application.dto.common import IdResponse
from bidhub.application.usecases.user import AuthenticateUser
from bidhub.core.models import UserId


@inject
async def login(
    *,
    usecase: FromDishka[AuthenticateUser],
    jwt_processor: FromDishka[JwtProcessor],
    login_data: AuthenticateUserRequest,
    response: Response,
) -> IdResponse[UserId]:
    """
    Logins user, sets JWT cookie, returns user data.\n\n

    ### Returns 400:
        * When user doesn't exist
        * When password is incorrect
    """
    user = await usecase(login_data)
    token = jwt_processor.encode(user.id, expires_in=JWT_COOKIE_LIFETIME)
    response.set_cookie(
        key=JWT_COOKIE_NAME,
        value=token,
        expires=JWT_COOKIE_LIFETIME,
        httponly=True,
    )
    return user
