from dishka.integrations.fastapi import FromDishka, inject

from bidhub.application.dto.user import UserResponse
from bidhub.application.usecases.user import GetUser
from bidhub.core.models import UserId


@inject
async def get_user(
    *,
    user_id: UserId,
    usecase: FromDishka[GetUser],
) -> UserResponse:
    """
    Returns some user data.\n\n

    ### Returns 404:
        * When user is not found
    ### Returns 429:
        * When rate limit is exceeded
    """
    user = await usecase(user_id)
    return user
