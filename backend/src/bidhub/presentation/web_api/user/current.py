from dishka.integrations.fastapi import FromDishka, inject

from bidhub.presentation.auth_guard import WithAuth
from bidhub.application.dto.user import UserResponse
from bidhub.application.usecases.user import GetCurrentUser
from bidhub.application.protocols.security import IUserIdentity


@inject
async def get_current_user(
    *,
    identity: FromDishka[IUserIdentity],
    initialize_usecase: FromDishka[WithAuth[GetCurrentUser]],
) -> UserResponse:
    usecase = initialize_usecase(identity)
    user = await usecase()
    return user
