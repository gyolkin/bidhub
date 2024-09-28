from dataclasses import dataclass, field
from datetime import datetime
from typing import NewType
from uuid import UUID


UserId = NewType('UserId', UUID)


@dataclass
class User:
    id: UserId = field(init=False)
    email: str
    password: str
    is_admin: bool
    created_at: datetime

    def set_password(self, hashed_password: str) -> None:
        self.password = hashed_password
