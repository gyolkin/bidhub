from datetime import datetime
from dataclasses import dataclass

from bidhub.core.models import Auction, AuctionId, UserId, User

from .user import UserOutput
from .common import PaginationFilter


@dataclass(frozen=True, slots=True)
class ListAuctionsFilter(PaginationFilter):
    user_id: UserId | None = None
    is_active: bool | None = None


@dataclass(frozen=True, slots=True)
class CreateAuctionInput:
    title: str
    description: str
    start_price: int
    mins_to_finish: int


@dataclass(frozen=True, slots=True)
class AuctionOutput:
    id: AuctionId
    user: UserOutput
    title: str
    description: str
    start_price: int
    created_at: datetime
    ending_at: datetime
    is_active: bool


@dataclass(frozen=True, slots=True)
class AuctionIdOutput:
    id: AuctionId


def map_auction_to_dto(auction: Auction, user: User) -> AuctionOutput:
    user_dto = UserOutput(
        id=user.id,
        email=user.email,
        is_admin=user.is_admin,
        created_at=user.created_at,
    )
    return AuctionOutput(
        id=auction.id,
        user=user_dto,
        title=auction.title,
        description=auction.description,
        start_price=auction.start_price,
        created_at=auction.created_at,
        ending_at=auction.ending_at,
        is_active=auction.is_active,
    )
