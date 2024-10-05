from abc import ABC, abstractmethod

from bidhub.application.dto.auction import DetailedAuctionResponse, ShortAuctionResponse, ListAuctionsFilter
from bidhub.core.models import AuctionId


class IAuctionTable(ABC):
    @abstractmethod
    async def get_detailed_auction_by_id(self, auction_id: AuctionId) -> DetailedAuctionResponse | None:
        raise NotImplementedError

    @abstractmethod
    async def list_auctions_with_total(self, filters: ListAuctionsFilter) -> tuple[list[ShortAuctionResponse], int]:
        raise NotImplementedError
