from dishka.integrations.fastapi import inject, FromDishka
from fastapi import Query, Depends

from bidhub.presentation.web_api.pagination import get_pagination
from bidhub.application.dto.bid import DetailedBidResponse, ListBidsFilter
from bidhub.application.dto.common import PaginatedItemsResponse, PaginationFilter
from bidhub.application.usecases.bid import ListBids
from bidhub.core.models import AuctionId, UserId


@inject
async def list_bids(
    usecase: FromDishka[ListBids],
    user_id: UserId | None = Query(None),
    auction_id: AuctionId | None = Query(None),
    pagination: PaginationFilter = Depends(get_pagination),
) -> PaginatedItemsResponse[DetailedBidResponse]:
    filters = ListBidsFilter(
        pagination=pagination,
        auction_id=auction_id,
        user_id=user_id,
    )
    bids = await usecase(filters)
    return bids
