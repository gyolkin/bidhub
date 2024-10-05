from sqlalchemy.ext.asyncio import AsyncSession

from bidhub.application.protocols.persistence import IBidGateway
from bidhub.core.models import Bid, BidId


class SqlaBidGateway(IBidGateway):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_bid_by_id(self, bid_id: BidId) -> Bid | None:
        bid = await self.session.get(Bid, bid_id)
        return bid

    async def save_bid(self, bid: Bid) -> None:
        self.session.add(bid)
