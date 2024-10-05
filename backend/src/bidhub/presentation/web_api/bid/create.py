from dishka.integrations.fastapi import inject, FromDishka
from fastapi import Query

from bidhub.presentation.auth_guard import WithAuth
from bidhub.application.dto.bid import CreateBidRequest
from bidhub.application.dto.common import IdResponse
from bidhub.application.usecases.bid import PlaceBid
from bidhub.application.protocols.security import IUserIdentity
from bidhub.core.models import AuctionId, BidId


@inject
async def create_bid(
    *,
    initialize_usecase: FromDishka[WithAuth[PlaceBid]],
    identity: FromDishka[IUserIdentity],
    bid_data: CreateBidRequest,
    auction_id: AuctionId = Query(),
) -> IdResponse[BidId]:
    usecase = initialize_usecase(identity)
    bid = await usecase(auction_id, bid_data)
    return bid
