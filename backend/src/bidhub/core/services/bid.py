from datetime import datetime

from bidhub.core.models import Bid, UserId, AuctionId


class BidService:
    def create_bid(
        self,
        *,
        user_id: UserId,
        auction_id: AuctionId,
        amount: int,
    ) -> Bid:
        created_at = datetime.now()
        return Bid(
            user_id=user_id,
            auction_id=auction_id,
            amount=amount,
            created_at=created_at,
        )
