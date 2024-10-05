from sqlalchemy.ext.asyncio import AsyncSession

from bidhub.application.protocols.persistence import IAuctionGateway
from bidhub.core.models import Auction, AuctionId


class SqlaAuctionGateway(IAuctionGateway):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_auction_by_id(self, auction_id: AuctionId) -> Auction | None:
        auction = await self.session.get(Auction, auction_id)
        return auction

    async def save_auction(self, auction: Auction) -> None:
        self.session.add(auction)

    async def update_auction(self, auction: Auction) -> None:
        self.session.add(auction)
