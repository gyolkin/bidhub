from abc import ABC, abstractmethod

from bidhub.core.models import Bid, BidId


class IBidGateway(ABC):
    @abstractmethod
    async def get_bid_by_id(self, bid_id: BidId) -> Bid | None:
        raise NotImplementedError

    @abstractmethod
    async def save_bid(self, bid: Bid) -> None:
        raise NotImplementedError
