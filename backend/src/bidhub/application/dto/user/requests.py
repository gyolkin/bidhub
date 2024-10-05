from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CreateUserRequest:
    password: str
    email: str


@dataclass(frozen=True, slots=True)
class UpdateUserRequest:
    password: str | None = None


@dataclass(frozen=True, slots=True)
class AuthenticateUserRequest:
    email: str
    password: str
