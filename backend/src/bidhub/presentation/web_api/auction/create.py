from dishka.integrations.fastapi import inject, FromDishka

from bidhub.presentation.auth_guard import WithAuth
from bidhub.application.dto.auction import CreateAuctionInput
from bidhub.application.dto.common import IdResponse
from bidhub.application.usecases.auction import StartAuction
from bidhub.application.protocols.security import IUserIdentity
from bidhub.core.models import AuctionId


@inject
async def create_auction(
    *,
    initialize_usecase: FromDishka[WithAuth[StartAuction]],
    identity: FromDishka[IUserIdentity],
    auction_data: CreateAuctionInput,
) -> IdResponse[AuctionId]:
    usecase = initialize_usecase(identity)
    auction = await usecase(auction_data)
    return auction
