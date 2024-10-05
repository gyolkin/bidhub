from dishka.integrations.fastapi import inject, FromDishka
from fastapi import Query, Depends

from bidhub.presentation.web_api.pagination import get_pagination
from bidhub.application.dto.auction import ShortAuctionResponse, ListAuctionsFilter
from bidhub.application.dto.common import PaginatedItemsResponse, PaginationFilter
from bidhub.application.usecases.auction import ListAuctions
from bidhub.core.models import UserId


@inject
async def list_auctions(
    usecase: FromDishka[ListAuctions],
    user_id: UserId | None = Query(None),
    is_active: bool | None = Query(None),
    pagination: PaginationFilter = Depends(get_pagination),
) -> PaginatedItemsResponse[ShortAuctionResponse]:
    filters = ListAuctionsFilter(
        pagination=pagination,
        user_id=user_id,
        is_active=is_active,
    )
    auctions = await usecase(filters)
    return auctions
