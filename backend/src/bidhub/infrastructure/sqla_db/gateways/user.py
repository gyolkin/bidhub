from typing import Iterable, Sequence

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from bidhub.application.protocols.persistence import IUserGateway
from bidhub.core.models import UserId, User


class SqlaUserGateway(IUserGateway):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_by_id(self, user_id: UserId) -> User | None:
        user = await self.session.get(User, user_id)
        return user

    async def get_user_by_email(self, email: str) -> User | None:
        query = sa.select(User).where(User.email == email)
        result = await self.session.execute(query)
        user = result.scalars().first()
        return user

    async def list_users_by_ids(self, user_ids: Iterable[UserId]) -> Sequence[User]:
        query = sa.select(User).where(User.id.in_(user_ids))
        result = await self.session.execute(query)
        users = result.scalars().all()
        return users

    async def save_user(self, user: User) -> None:
        self.session.add(user)

    async def update_user(self, user: User) -> None:
        self.session.add(user)
