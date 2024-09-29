from dishka.integrations.fastapi import inject, FromDishka
from fastapi import Query

from bidhub.application.dto.bid import BidOutput, ListBidsFilter
from bidhub.application.dto.common import PaginatedItemsOutput
from bidhub.application.usecases.bid import ListBids
from bidhub.core.models import AuctionId, UserId


@inject
async def list_bids(
    usecase: FromDishka[ListBids],
    user_id: UserId | None = Query(None),
    auction_id: AuctionId | None = Query(None),
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1),
) -> PaginatedItemsOutput[BidOutput]:
    filters = ListBidsFilter(
        auction_id=auction_id,
        user_id=user_id,
        page=page,
        per_page=per_page,
    )
    auctions = await usecase(filters)
    return auctions
