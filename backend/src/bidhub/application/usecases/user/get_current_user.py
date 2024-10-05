from bidhub.application.dto.user import UserResponse
from bidhub.application.protocols.security import IUserIdentity


class GetCurrentUser:
    def __init__(
        self,
        *,
        user_identity: IUserIdentity,
    ):
        self.user_identity = user_identity

    async def __call__(self) -> UserResponse:
        user = await self.user_identity.get_current_user()
        return UserResponse(
            id=user.id,
            email=user.email,
            is_admin=user.is_admin,
            created_at=user.created_at,
        )
