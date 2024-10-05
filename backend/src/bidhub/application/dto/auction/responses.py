from datetime import datetime
from dataclasses import dataclass

from bidhub.application.dto.user import UserResponse
from bidhub.core.models import AuctionId, UserId, BidId


@dataclass(frozen=True, slots=True)
class HighestBidResponse:
    id: BidId
    user: UserResponse
    amount: int
    created_at: datetime


@dataclass(frozen=True, slots=True)
class DetailedAuctionResponse:
    id: AuctionId
    user: UserResponse
    title: str
    description: str
    start_price: int
    created_at: datetime
    ending_at: datetime
    is_active: bool
    total_bids: int
    highest_bid: HighestBidResponse | None


@dataclass(frozen=True, slots=True)
class ShortAuctionResponse:
    id: AuctionId
    user_id: UserId
    highest_bid_amount: int
    total_bids: int
    title: str
    start_price: int
    created_at: datetime
    ending_at: datetime
    is_active: bool
