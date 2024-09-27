from dataclasses import dataclass, field
from datetime import datetime
from typing import NewType
from uuid import UUID

from .user import UserId


AuctionId = NewType('AuctionId', UUID)


@dataclass
class Auction:
    id: AuctionId = field(init=False)
    user_id: UserId
    title: str
    description: str
    start_price: int
    created_at: datetime
    ending_at: datetime
    is_active: bool

    def close_auction(self) -> None:
        self.is_active = False
