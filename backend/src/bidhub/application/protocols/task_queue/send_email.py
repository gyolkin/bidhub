from abc import ABC, abstractmethod

from bidhub.application.dto.task_queue import SendWelcomeEmailRequest


class ISendEmailTask(ABC):
    @abstractmethod
    async def __call__(
        self,
        *,
        message: SendWelcomeEmailRequest,
    ) -> None:
        raise NotImplementedError
