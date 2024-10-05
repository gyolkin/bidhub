import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from bidhub.infrastructure.sqla_db.pagination import apply_pagination
from bidhub.application.dto.bid import DetailedBidResponse, ListBidsFilter, BidAuctionResponse
from bidhub.application.dto.user import UserResponse
from bidhub.application.protocols.persistence import IBidTable
from bidhub.core.models import Bid, Auction, User


class SqlaBidTable(IBidTable):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list_bids_with_total(self, filters: ListBidsFilter) -> tuple[list[DetailedBidResponse], int]:
        query = (
            sa.select(
                Bid.id,
                Bid.user_id,
                Bid.auction_id,
                Bid.amount,
                Bid.created_at,
                Auction.id.label('auction_id'),
                Auction.title,
                Auction.is_active,
                User.id.label('user_id'),
                User.email.label('user_email'),
                User.is_admin.label('user_is_admin'),
                User.created_at.label('user_created_at'),
                sa.func.count().over().label('total_count'),
            )
            .join(Auction, Bid.auction_id == Auction.id)
            .join(User, Bid.user_id == User.id)
        )
        if filters.user_id is not None:
            query = query.where(Bid.user_id == filters.user_id)
        if filters.auction_id is not None:
            query = query.where(Bid.auction_id == filters.auction_id)
        query = query.order_by(Bid.created_at.desc())
        query = apply_pagination(query, filters.pagination)

        result = await self.session.execute(query)
        rows = result.fetchall()
        if not rows:
            return [], 0

        total_count = rows[0].total_count
        bids = [
            DetailedBidResponse(
                id=row.id,
                user=UserResponse(
                    id=row.user_id,
                    email=row.user_email,
                    is_admin=row.user_is_admin,
                    created_at=row.user_created_at,
                ),
                auction=BidAuctionResponse(
                    id=row.auction_id,
                    title=row.title,
                    is_active=row.is_active,
                ),
                amount=row.amount,
                created_at=row.created_at,
            )
            for row in rows
        ]
        return bids, total_count
