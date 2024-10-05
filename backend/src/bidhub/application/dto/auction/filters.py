from dataclasses import dataclass

from bidhub.application.dto.common import PaginationFilter
from bidhub.core.models import UserId


@dataclass(frozen=True, slots=True)
class ListAuctionsFilter:
    pagination: PaginationFilter
    user_id: UserId | None
    is_active: bool | None
