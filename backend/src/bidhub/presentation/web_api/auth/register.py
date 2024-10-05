from dishka.integrations.fastapi import FromDishka, inject

from bidhub.application.dto.user import CreateUserRequest
from bidhub.application.dto.common import IdResponse
from bidhub.application.usecases.user import RegisterUser
from bidhub.core.models import UserId


@inject
async def register(
    *,
    usecase: FromDishka[RegisterUser],
    user_data: CreateUserRequest,
) -> IdResponse[UserId]:
    """
    Registers user, returns their id.\n\n

    ### Returns 400:
        * When email is already taken
        * When user data is not valid
    ### Returns 429:
        * When rate limit is exceeded
    """
    user = await usecase(user_data)
    return user
