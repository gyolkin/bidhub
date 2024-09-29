from dishka.integrations.fastapi import inject, FromDishka

from bidhub.application.dto.auction import AuctionOutput
from bidhub.application.usecases.auction import GetAuction
from bidhub.core.models import AuctionId


@inject
async def get_auction(
    auction_id: AuctionId,
    usecase: FromDishka[GetAuction],
) -> AuctionOutput:
    auction = await usecase(auction_id)
    return auction
