from bidhub.application.dto.user import UpdateUserRequest
from bidhub.application.dto.common import IdResponse
from bidhub.application.protocols.security import IPasswordManager, IUserIdentity
from bidhub.application.protocols.persistence import IUnitOfWork, IUserGateway
from bidhub.application.exceptions import NotFoundError
from bidhub.core.services import UserService, AccessService
from bidhub.core.models import UserId


class UpdateUser:
    def __init__(
        self,
        *,
        access_service: AccessService,
        user_identity: IUserIdentity,
        user_service: UserService,
        user_gateway: IUserGateway,
        uow: IUnitOfWork,
        password_manager: IPasswordManager,
    ):
        self.access_control = access_service
        self.user_identity = user_identity
        self.user_service = user_service
        self.user_gateway = user_gateway
        self.password_manager = password_manager
        self.uow = uow

    async def __call__(
        self,
        user_id: UserId,
        request: UpdateUserRequest,
    ) -> IdResponse[UserId]:
        current_user = await self.user_identity.get_current_user()
        user = await self.user_gateway.get_user_by_id(user_id)
        if not user:
            raise NotFoundError()
        self.access_control.allow_user_update(actor=current_user, resource=user)
        self.user_service.update_user(user, password=request.password)
        if request.password is not None:
            hashed_password = await self.password_manager.hash(user.password)
            user.set_password(hashed_password)
        await self.user_gateway.update_user(user)
        await self.uow.commit()
        return IdResponse(user.id)
