from dishka.integrations.fastapi import inject, FromDishka
from fastapi import Query

from bidhub.presentation.auth_guard import WithAuth
from bidhub.application.dto.bid import BidIdOutput, CreateBidInput
from bidhub.application.usecases.bid import PlaceBid
from bidhub.application.protocols.security import IUserIdentity
from bidhub.core.models import AuctionId


@inject
async def create_bid(
    *,
    initialize_usecase: FromDishka[WithAuth[PlaceBid]],
    identity: FromDishka[IUserIdentity],
    bid_data: CreateBidInput,
    auction_id: AuctionId = Query(),
) -> BidIdOutput:
    usecase = initialize_usecase(identity)
    bid = await usecase(auction_id, bid_data)
    return bid
