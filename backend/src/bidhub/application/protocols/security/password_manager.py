from abc import ABC, abstractmethod


class IPasswordManager(ABC):
    @abstractmethod
    async def hash(self, password: str) -> str:
        raise NotImplementedError

    @abstractmethod
    async def verify(self, hash: str, password: str) -> bool:
        raise NotImplementedError
