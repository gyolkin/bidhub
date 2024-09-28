from typing import Iterable, Sequence
from abc import ABC, abstractmethod

from bidhub.core.models import UserId, User


class IUserGateway(ABC):
    @abstractmethod
    async def get_user_by_id(self, user_id: UserId) -> User | None:
        raise NotImplementedError

    @abstractmethod
    async def list_users_by_ids(self, user_ids: Iterable[UserId]) -> Sequence[User]:
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_email(self, email: str) -> User | None:
        raise NotImplementedError

    @abstractmethod
    async def save_user(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    async def update_user(self, user: User) -> None:
        raise NotImplementedError
