from datetime import datetime

from bidhub.core.models import User
from bidhub.core.validators import PasswordValidator, EmailValidator


class UserService:
    def __init__(
        self,
        password_validator: PasswordValidator,
        email_validator: EmailValidator,
    ):
        self.validate_password = password_validator
        self.validate_email = email_validator

    def create_user(
        self,
        *,
        email: str,
        password: str,
        is_admin: bool,
    ) -> User:
        self.validate_email(email)
        self.validate_password(password)
        created_at = datetime.now()
        return User(
            email=email,
            password=password,
            is_admin=is_admin,
            created_at=created_at,
        )

    def update_user(
        self,
        user: User,
        *,
        password: str | None = None,
        is_admin: bool | None = None,
    ) -> None:
        if password is not None:
            self.validate_password(password)
            user.password = password
        if is_admin is not None:
            user.is_admin = is_admin
