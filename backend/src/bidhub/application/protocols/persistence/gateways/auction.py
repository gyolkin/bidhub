from abc import ABC, abstractmethod

from bidhub.core.models import Auction, AuctionId


class IAuctionGateway(ABC):
    @abstractmethod
    async def get_auction_by_id(self, auction_id: AuctionId) -> Auction | None:
        raise NotImplementedError

    @abstractmethod
    async def save_auction(self, auction: Auction) -> None:
        raise NotImplementedError

    @abstractmethod
    async def update_auction(self, auction: Auction) -> None:
        raise NotImplementedError
