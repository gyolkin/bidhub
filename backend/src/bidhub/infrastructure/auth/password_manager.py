import asyncio
import bcrypt

from bidhub.application.protocols.security import IPasswordManager


HASH_ROUNDS = 12


class PasswordManager(IPasswordManager):
    async def hash(self, password: str) -> str:
        return await asyncio.to_thread(self._hash_sync, password)

    async def verify(self, hashed: str, password: str) -> bool:
        return await asyncio.to_thread(self._verify_sync, hashed, password)

    def _hash_sync(self, password: str) -> str:
        salt = bcrypt.gensalt(rounds=HASH_ROUNDS)
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def _verify_sync(self, hashed: str, password: str) -> bool:
        try:
            return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
        except ValueError:
            return False
