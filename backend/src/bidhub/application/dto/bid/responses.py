from datetime import datetime
from dataclasses import dataclass

from bidhub.application.dto.user import UserResponse
from bidhub.core.models import BidId, AuctionId


@dataclass(frozen=True, slots=True)
class BidAuctionResponse:
    id: AuctionId
    title: str
    is_active: bool


@dataclass(frozen=True, slots=True)
class DetailedBidResponse:
    id: BidId
    user: UserResponse
    auction: BidAuctionResponse
    amount: int
    created_at: datetime
