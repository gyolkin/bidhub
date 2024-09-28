from datetime import datetime
from dataclasses import dataclass

from bidhub.core.models import User, UserId


@dataclass(frozen=True, slots=True)
class CreateUserInput:
    password: str
    email: str


@dataclass(frozen=True, slots=True)
class UpdateUserInput:
    password: str | None = None


@dataclass(frozen=True, slots=True)
class AuthenticateUserInput:
    email: str
    password: str


@dataclass(frozen=True, slots=True)
class UserOutput:
    id: UserId
    email: str
    is_admin: bool
    created_at: datetime


@dataclass(frozen=True, slots=True)
class UserIdOutput:
    id: UserId


def map_user_to_dto(user: User) -> UserOutput:
    return UserOutput(
        id=user.id,
        email=user.email,
        created_at=user.created_at,
        is_admin=user.is_admin,
    )
