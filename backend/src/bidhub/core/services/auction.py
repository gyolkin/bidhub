from datetime import datetime, timedelta

from bidhub.core.models import Auction, UserId


class AuctionService:
    def create_auction(
        self,
        *,
        user_id: UserId,
        title: str,
        description: str,
        start_price: int,
        days_to_finish: int,
    ) -> Auction:
        created_at = datetime.now()
        ending_at = created_at + timedelta(days=days_to_finish)
        return Auction(
            user_id=user_id,
            title=title,
            description=description,
            start_price=start_price,
            created_at=created_at,
            ending_at=ending_at,
            is_active=True,
        )
