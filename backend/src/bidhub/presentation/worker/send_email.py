from dishka.integrations.faststream import FromDishka, inject

from bidhub.application.dto.task_queue import SendWelcomeEmailRequest
from bidhub.application.usecases.task_queue import SendWelcomeEmail


@inject
async def send_welcome_email(
    usecase: FromDishka[SendWelcomeEmail],
    message: SendWelcomeEmailRequest,
) -> None:
    await usecase(message)
