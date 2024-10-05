from dataclasses import dataclass

from bidhub.application.dto.common import PaginationFilter
from bidhub.core.models import UserId, AuctionId


@dataclass(frozen=True, slots=True)
class ListBidsFilter:
    pagination: PaginationFilter
    user_id: UserId | None = None
    auction_id: AuctionId | None = None
