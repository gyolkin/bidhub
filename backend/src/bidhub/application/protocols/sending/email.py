from abc import ABC, abstractmethod


class IEmailSender(ABC):
    @abstractmethod
    async def __call__(
        self,
        *,
        email: str,
        subject: str,
        message: str,
    ) -> None:
        raise NotImplementedError
