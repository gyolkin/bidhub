from bidhub.infrastructure.exceptions import InfrastructureError
from bidhub.application.protocols.persistence import IUserGateway
from bidhub.application.protocols.security import IUserIdentity
from bidhub.core.models import User, UserId

from .jwt_processor import JwtProcessor


TOKEN_NOT_PROVIDED = 'Please provide a valid token.'
USER_DOES_NOT_EXIST_ANYMORE = 'This user does not exist anymore.'


class TokenUserIdentityProvider(IUserIdentity):
    def __init__(
        self,
        user_gateway: IUserGateway,
        token_processor: JwtProcessor,
        token: str | None,
    ):
        self.user_gateway = user_gateway
        self.token_processor = token_processor
        self.token = token

    async def get_current_user(self) -> User:
        if not self.token:
            raise InfrastructureError(TOKEN_NOT_PROVIDED)
        current_user_id = self.token_processor.decode(self.token)
        return await self._get_user(current_user_id)

    async def get_current_user_or_none(self) -> User | None:
        if not self.token:
            return None
        current_user_id = self.token_processor.decode(self.token)
        return await self._get_user(current_user_id)

    async def _get_user(self, current_user_id: UserId) -> User:
        current_user = await self.user_gateway.get_user_by_id(current_user_id)
        if not current_user:
            raise InfrastructureError(USER_DOES_NOT_EXIST_ANYMORE)
        return current_user
