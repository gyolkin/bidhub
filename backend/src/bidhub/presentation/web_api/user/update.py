from dishka.integrations.fastapi import FromDishka, inject

from bidhub.presentation.auth_guard import WithAuth
from bidhub.application.dto.user import UserIdOutput, UpdateUserInput
from bidhub.application.usecases.user import UpdateUser
from bidhub.application.protocols.security import IUserIdentity
from bidhub.core.models import UserId


@inject
async def update_user(
    *,
    user_id: UserId,
    user_data: UpdateUserInput,
    identity: FromDishka[IUserIdentity],
    initialize_usecase: FromDishka[WithAuth[UpdateUser]],
) -> UserIdOutput:
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
