from abc import ABC, abstractmethod

from bidhub.core.models import User, Auction, Bid


class INotificationService(ABC):
    @abstractmethod
    async def notify_auction_finished_no_bids(self, owner: User, auction: Auction) -> None:
        raise NotImplementedError

    @abstractmethod
    async def notify_auction_finished_with_winner(self, owner: User, auction: Auction, highest_bid: Bid) -> None:
        raise NotImplementedError

    @abstractmethod
    async def notify_auction_winner(self, winner: User, auction: Auction) -> None:
        raise NotImplementedError
