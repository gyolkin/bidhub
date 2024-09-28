from bidhub.application.dto.user import CreateUserInput, UserIdOutput
from bidhub.application.dto.task_queue import SendWelcomeEmailInput
from bidhub.application.protocols.persistence import IUnitOfWork, IUserGateway
from bidhub.application.protocols.task_queue import ISendEmailTask
from bidhub.application.protocols.security import IPasswordManager
from bidhub.application.exceptions import AlreadyExistsError
from bidhub.core.services import UserService


class RegisterUser:
    def __init__(
        self,
        *,
        user_service: UserService,
        user_gateway: IUserGateway,
        uow: IUnitOfWork,
        send_email_task: ISendEmailTask,
        password_manager: IPasswordManager,
    ):
        self.user_service = user_service
        self.user_gateway = user_gateway
        self.uow = uow
        self.password_manager = password_manager
        self.send_email_task = send_email_task

    async def __call__(self, request: CreateUserInput) -> UserIdOutput:
        user = await self.user_gateway.get_user_by_email(request.email)
        if user:
            raise AlreadyExistsError()
        new_user = self.user_service.create_user(
            email=request.email,
            password=request.password,
            is_admin=False,
        )
        hashed_password = await self.password_manager.hash(new_user.password)
        new_user.set_password(hashed_password)
        await self.user_gateway.save_user(new_user)
        await self.uow.commit()
        await self._send_welcome_email(new_user.email)
        return UserIdOutput(new_user.id)

    async def _send_welcome_email(self, email: str):
        message = SendWelcomeEmailInput(receiver=email)
        await self.send_email_task(message=message)
