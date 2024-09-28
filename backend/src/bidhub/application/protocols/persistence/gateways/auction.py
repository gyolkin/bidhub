from typing import Iterable, Sequence
from abc import ABC, abstractmethod

from bidhub.application.dto.auction import ListAuctionsFilter
from bidhub.core.models import Auction, AuctionId


class IAuctionGateway(ABC):
    @abstractmethod
    async def get_auction_by_id(self, auction_id: AuctionId) -> Auction | None:
        raise NotImplementedError

    @abstractmethod
    async def list_auctions_by_ids(self, auction_ids: Iterable[AuctionId]) -> Auction | None:
        raise NotImplementedError

    @abstractmethod
    async def list_auctions(self, filters: ListAuctionsFilter) -> tuple[Sequence[Auction], int]:
        raise NotImplementedError

    @abstractmethod
    async def save_auction(self, auction: Auction) -> None:
        raise NotImplementedError

    @abstractmethod
    async def update_auction(self, auction: Auction) -> None:
        raise NotImplementedError
