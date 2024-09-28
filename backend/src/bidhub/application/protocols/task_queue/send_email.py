from abc import ABC, abstractmethod

from bidhub.application.dto.task_queue import SendWelcomeEmailInput


class ISendEmailTask(ABC):
    @abstractmethod
    async def __call__(
        self,
        *,
        message: SendWelcomeEmailInput,
    ) -> None:
        raise NotImplementedError
