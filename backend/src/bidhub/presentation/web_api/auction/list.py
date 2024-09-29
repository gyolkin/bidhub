from dishka.integrations.fastapi import inject, FromDishka
from fastapi import Query

from bidhub.application.dto.auction import AuctionOutput, ListAuctionsFilter
from bidhub.application.dto.common import PaginatedItemsOutput
from bidhub.application.usecases.auction import ListAuctions
from bidhub.core.models import UserId


@inject
async def list_auctions(
    usecase: FromDishka[ListAuctions],
    user_id: UserId | None = Query(None),
    is_active: bool | None = Query(None),
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1),
) -> PaginatedItemsOutput[AuctionOutput]:
    filters = ListAuctionsFilter(
        user_id=user_id,
        is_active=is_active,
        page=page,
        per_page=per_page,
    )
    auctions = await usecase(filters)
    return auctions
