from dataclasses import dataclass, field
from datetime import datetime
from typing import NewType
from uuid import UUID

from .user import UserId
from .auction import AuctionId


BidId = NewType('BidId', UUID)


@dataclass
class Bid:
    id: BidId = field(init=False)
    auction_id: AuctionId
    user_id: UserId
    amount: int
    created_at: datetime
