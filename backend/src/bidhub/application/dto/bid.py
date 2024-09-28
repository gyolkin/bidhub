from datetime import datetime
from dataclasses import dataclass

from bidhub.core.models import Bid, BidId, UserId, User, AuctionId

from .user import UserOutput, map_user_to_dto
from .common import PaginationFilter


@dataclass(frozen=True, slots=True)
class ListBidsFilter(PaginationFilter):
    user_id: UserId | None = None
    auction_id: AuctionId | None = None


@dataclass(frozen=True, slots=True)
class CreateBidInput:
    amount: int


@dataclass(frozen=True, slots=True)
class BidOutput:
    id: BidId
    user: UserOutput
    auction_id: AuctionId
    amount: int
    created_at: datetime


@dataclass(frozen=True, slots=True)
class BidIdOutput:
    id: BidId


def map_auction_bids_to_dto(bid: Bid, user: User) -> BidOutput:
    return BidOutput(
        id=bid.id,
        user=map_user_to_dto(user),
        auction_id=bid.auction_id,
        amount=bid.amount,
        created_at=bid.created_at,
    )
