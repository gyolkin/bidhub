from abc import ABC, abstractmethod

from bidhub.core.models import User


class IUserIdentity(ABC):
    @abstractmethod
    async def get_current_user(self) -> User:
        raise NotImplementedError

    @abstractmethod
    async def get_current_user_or_none(self) -> User | None:
        raise NotImplementedError
