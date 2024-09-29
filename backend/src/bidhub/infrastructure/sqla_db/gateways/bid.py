from typing import Sequence, Iterable
from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa

from bidhub.application.dto.bid import ListBidsFilter
from bidhub.application.protocols.persistence import IBidGateway
from bidhub.core.models import AuctionId, Bid, BidId


class SqlaBidGateway(IBidGateway):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_bid_by_id(self, bid_id: BidId) -> Bid | None:
        bid = await self.session.get(Bid, bid_id)
        return bid

    async def get_highest_bid_by_auction(self, auction_id: AuctionId) -> Bid | None:
        query = sa.select(Bid).where(Bid.auction_id == auction_id).order_by(Bid.amount.desc())
        result = await self.session.execute(query)
        bid = result.scalars().first()
        return bid

    async def list_bids_by_ids(self, bid_ids: Iterable[BidId]) -> Sequence[Bid]:
        query = sa.select(Bid).where(Bid.id.in_(bid_ids))
        result = await self.session.execute(query)
        bids = result.scalars().all()
        return bids

    async def list_bids(self, filters: ListBidsFilter) -> tuple[Sequence[Bid], int]:
        query = sa.select(Bid)
        if filters.auction_id is not None:
            query = query.where(Bid.auction_id == filters.auction_id)
        if filters.user_id is not None:
            query = query.where(Bid.user_id == filters.user_id)
        total_query = sa.select(sa.func.count()).select_from(query.subquery())
        total = await self.session.scalar(total_query)
        offset = (filters.page - 1) * filters.per_page
        query = query.offset(offset).limit(filters.per_page)
        result = await self.session.execute(query)
        bids = result.scalars().all()
        return bids, total or 0

    async def save_bid(self, bid: Bid) -> None:
        self.session.add(bid)
