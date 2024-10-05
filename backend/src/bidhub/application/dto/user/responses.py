from datetime import datetime
from dataclasses import dataclass

from bidhub.core.models import UserId


@dataclass(frozen=True, slots=True)
class UserResponse:
    id: UserId
    email: str
    is_admin: bool
    created_at: datetime
