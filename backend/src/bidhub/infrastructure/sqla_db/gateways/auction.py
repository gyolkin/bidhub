from typing import Sequence, Iterable

from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa

from bidhub.application.protocols.persistence import IAuctionGateway
from bidhub.application.dto.auction import ListAuctionsFilter
from bidhub.core.models import Auction, AuctionId


class SqlaAuctionGateway(IAuctionGateway):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_auction_by_id(self, auction_id: AuctionId) -> Auction | None:
        auction = await self.session.get(Auction, auction_id)
        return auction

    async def list_auctions_by_ids(self, auction_ids: Iterable[AuctionId]) -> Sequence[Auction]:
        query = sa.select(Auction).where(Auction.id.in_(auction_ids))
        result = await self.session.execute(query)
        auctions = result.scalars().all()
        return auctions

    async def list_auctions(self, filters: ListAuctionsFilter) -> tuple[Sequence[Auction], int]:
        query = sa.select(Auction)
        if filters.user_id is not None:
            query = query.where(Auction.user_id == filters.user_id)
        if filters.is_active is not None:
            query = query.where(Auction.is_active == filters.is_active)
        total_query = sa.select(sa.func.count()).select_from(query.subquery())
        total = await self.session.scalar(total_query)
        offset = (filters.page - 1) * filters.per_page
        query = query.offset(offset).limit(filters.per_page)
        result = await self.session.execute(query)
        auctions = result.scalars().all()
        return auctions, total or 0

    async def save_auction(self, auction: Auction) -> None:
        self.session.add(auction)

    async def update_auction(self, auction: Auction) -> None:
        self.session.add(auction)
