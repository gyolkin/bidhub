import sqlalchemy as sa
from sqlalchemy.orm import aliased
from sqlalchemy.ext.asyncio import AsyncSession

from bidhub.infrastructure.sqla_db.pagination import apply_pagination
from bidhub.application.dto.auction import (
    DetailedAuctionResponse,
    ShortAuctionResponse,
    ListAuctionsFilter,
    HighestBidResponse,
)
from bidhub.application.dto.user import UserResponse
from bidhub.application.protocols.persistence import IAuctionTable
from bidhub.core.models import AuctionId, Auction, Bid, User


class SqlaAuctionTable(IAuctionTable):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_detailed_auction_by_id(self, auction_id: AuctionId) -> DetailedAuctionResponse | None:
        highest_bid_subquery = self._get_highest_bid_subquery(auction_id)
        total_bids_subquery = self._get_total_bids_subquery(auction_id)

        HighestBidUser = aliased(User)
        query = (
            sa.select(
                Auction.id,
                Auction.title,
                Auction.description,
                Auction.start_price,
                Auction.created_at,
                Auction.ending_at,
                Auction.is_active,
                total_bids_subquery.label('total_bids'),
                User.id.label('user_id'),
                User.email.label('user_email'),
                User.is_admin.label('user_is_admin'),
                User.created_at.label('user_created_at'),
                highest_bid_subquery.c.highest_bid_id,
                highest_bid_subquery.c.highest_bid_amount,
                highest_bid_subquery.c.highest_bid_created_at,
                HighestBidUser.id.label('highest_bid_user_id'),
                HighestBidUser.email.label('highest_bid_user_email'),
                HighestBidUser.is_admin.label('highest_bid_user_is_admin'),
                HighestBidUser.created_at.label('highest_bid_user_created_at'),
            )
            .join(User, Auction.user_id == User.id)
            .outerjoin(highest_bid_subquery, highest_bid_subquery.c.auction_id == Auction.id)
            .outerjoin(HighestBidUser, highest_bid_subquery.c.highest_bid_user_id == HighestBidUser.id)
            .where(Auction.id == auction_id)
        )

        result = await self.session.execute(query)
        row = result.fetchone()
        if row is None:
            return None

        highest_bid = None
        if row.highest_bid_id:
            highest_bid_user = UserResponse(
                id=row.highest_bid_user_id,
                email=row.highest_bid_user_email,
                is_admin=row.highest_bid_user_is_admin,
                created_at=row.highest_bid_user_created_at,
            )
            highest_bid = HighestBidResponse(
                id=row.highest_bid_id,
                user=highest_bid_user,
                amount=row.highest_bid_amount,
                created_at=row.highest_bid_created_at,
            )
        user = UserResponse(
            id=row.user_id,
            email=row.user_email,
            is_admin=row.user_is_admin,
            created_at=row.user_created_at,
        )
        return DetailedAuctionResponse(
            id=row.id,
            user=user,
            highest_bid=highest_bid,
            title=row.title,
            description=row.description,
            start_price=row.start_price,
            created_at=row.created_at,
            ending_at=row.ending_at,
            is_active=row.is_active,
            total_bids=row.total_bids,
        )

    async def list_auctions_with_total(self, filters: ListAuctionsFilter) -> tuple[list[ShortAuctionResponse], int]:
        highest_bid_subquery = self._get_highest_bid_subquery()
        total_bids_subquery = self._get_total_bids_subquery()

        query = (
            sa.select(
                Auction.id,
                Auction.user_id,
                Auction.title,
                Auction.start_price,
                Auction.created_at,
                Auction.ending_at,
                Auction.is_active,
                sa.func.coalesce(highest_bid_subquery.c.highest_bid_amount, 0).label('highest_bid_amount'),
                sa.func.coalesce(total_bids_subquery.c.total_bids, 0).label('total_bids'),
                sa.func.count().over().label('total_count'),
            )
            .outerjoin(highest_bid_subquery, Auction.id == highest_bid_subquery.c.auction_id)
            .outerjoin(total_bids_subquery, Auction.id == total_bids_subquery.c.auction_id)
        )
        if filters.user_id is not None:
            query = query.where(Auction.user_id == filters.user_id)
        if filters.is_active is not None:
            query = query.where(Auction.is_active == filters.is_active)
        query = query.order_by(Auction.created_at.desc())
        query = apply_pagination(query, filters.pagination)

        result = await self.session.execute(query)
        rows = result.fetchall()
        if not rows:
            return [], 0

        total_count = rows[0].total_count
        auctions = [
            ShortAuctionResponse(
                id=row.id,
                user_id=row.user_id,
                highest_bid_amount=row.highest_bid_amount,
                total_bids=row.total_bids,
                title=row.title,
                start_price=row.start_price,
                created_at=row.created_at,
                ending_at=row.ending_at,
                is_active=row.is_active,
            )
            for row in rows
        ]
        return auctions, total_count

    def _get_highest_bid_subquery(self, auction_id: AuctionId | None = None):
        if auction_id is None:
            return (
                sa.select(Bid.auction_id, sa.func.max(Bid.amount).label('highest_bid_amount'))
                .group_by(Bid.auction_id)
                .subquery()
            )
        return (
            sa.select(
                Bid.id.label('highest_bid_id'),
                Bid.amount.label('highest_bid_amount'),
                Bid.created_at.label('highest_bid_created_at'),
                Bid.user_id.label('highest_bid_user_id'),
                Bid.auction_id.label('auction_id'),
            )
            .where(Bid.auction_id == auction_id)
            .order_by(Bid.amount.desc(), Bid.created_at.asc())
            .limit(1)
            .subquery()
        )

    def _get_total_bids_subquery(self, auction_id: AuctionId | None = None):
        if auction_id is None:
            return (
                sa.select(Bid.auction_id, sa.func.count(Bid.id).label('total_bids')).group_by(Bid.auction_id).subquery()
            )
        return sa.select(sa.func.count(Bid.id)).where(Bid.auction_id == auction_id).scalar_subquery()
