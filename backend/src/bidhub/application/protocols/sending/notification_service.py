from abc import ABC, abstractmethod

from bidhub.application.dto.user import UserResponse


class INotificationService(ABC):
    @abstractmethod
    async def notify_auction_finished_no_bids(
        self,
        owner_email: str,
        auction_title: str,
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    async def notify_auction_finished_with_winner(
        self,
        owner_email: str,
        auction_title: str,
        highest_bid_amount: int,
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    async def notify_auction_winner(self, winner_email: str, auction_title: str) -> None:
        raise NotImplementedError
