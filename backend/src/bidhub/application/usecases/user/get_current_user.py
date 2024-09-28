from bidhub.application.dto.user import UserOutput, map_user_to_dto
from bidhub.application.protocols.security import IUserIdentity


class GetCurrentUser:
    def __init__(
        self,
        *,
        user_identity: IUserIdentity,
    ):
        self.user_identity = user_identity

    async def __call__(self) -> UserOutput:
        user = await self.user_identity.get_current_user()
        return map_user_to_dto(user)
