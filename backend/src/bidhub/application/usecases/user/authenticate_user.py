from bidhub.application.dto.user import AuthenticateUserRequest
from bidhub.application.dto.common import IdResponse
from bidhub.application.protocols.persistence import IUserGateway
from bidhub.application.protocols.security import IPasswordManager
from bidhub.application.exceptions import AuthenticationError
from bidhub.core.models import UserId


class AuthenticateUser:
    def __init__(
        self,
        *,
        user_gateway: IUserGateway,
        password_manager: IPasswordManager,
    ):
        self.user_gateway = user_gateway
        self.password_manager = password_manager

    async def __call__(self, request: AuthenticateUserRequest) -> IdResponse[UserId]:
        user = await self.user_gateway.get_user_by_email(request.email)
        if not user or not await self.password_manager.verify(user.password, request.password):
            raise AuthenticationError()
        return IdResponse(user.id)
