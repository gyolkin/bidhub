from typing import Iterable, Sequence
from abc import ABC, abstractmethod

from bidhub.application.dto.bid import ListBidsFilter
from bidhub.core.models import AuctionId, Bid, BidId


class IBidGateway(ABC):
    @abstractmethod
    async def get_bid_by_id(self, bid_id: BidId) -> Bid | None:
        raise NotImplementedError

    @abstractmethod
    async def get_highest_bid_by_auction(self, auction_id: AuctionId) -> Bid | None:
        raise NotImplementedError

    @abstractmethod
    async def list_bids_by_ids(self, bid_id: Iterable[BidId]) -> Sequence[Bid]:
        raise NotImplementedError

    @abstractmethod
    async def list_bids(self, filters: ListBidsFilter) -> tuple[Sequence[Bid], int]:
        raise NotImplementedError

    @abstractmethod
    async def save_bid(self, bid: Bid) -> None:
        raise NotImplementedError
