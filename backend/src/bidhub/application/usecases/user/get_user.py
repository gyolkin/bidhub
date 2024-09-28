from bidhub.application.dto.user import UserOutput, map_user_to_dto
from bidhub.application.protocols.persistence import IUserGateway
from bidhub.application.exceptions import NotFoundError
from bidhub.core.models import UserId


class GetUser:
    def __init__(
        self,
        *,
        user_gateway: IUserGateway,
    ):
        self.user_gateway = user_gateway

    async def __call__(self, user_id: UserId) -> UserOutput:
        user = await self.user_gateway.get_user_by_id(user_id)
        if user is None:
            raise NotFoundError()
        return map_user_to_dto(user)
