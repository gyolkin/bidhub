from dishka.integrations.fastapi import FromDishka, inject

from bidhub.presentation.auth_guard import WithAuth
from bidhub.application.dto.user import UpdateUserRequest
from bidhub.application.dto.common import IdResponse
from bidhub.application.usecases.user import UpdateUser
from bidhub.application.protocols.security import IUserIdentity
from bidhub.core.models import UserId


@inject
async def update_user(
    *,
    user_id: UserId,
    user_data: UpdateUserRequest,
    identity: FromDishka[IUserIdentity],
    initialize_usecase: FromDishka[WithAuth[UpdateUser]],
) -> IdResponse[UserId]:
    """
    Returns some user data.\n\n

    ### Returns 404:
        * When user is not found
    ### Returns 429:
        * When rate limit is exceeded
    """
    usecase = initialize_usecase(identity)
    user = await usecase(user_id, user_data)
    return user
