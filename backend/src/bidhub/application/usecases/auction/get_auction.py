from bidhub.application.exceptions import NotFoundError
from bidhub.application.dto.auction import AuctionOutput, map_auction_to_dto
from bidhub.application.protocols.persistence import IAuctionGateway, IUserGateway
from bidhub.core.models import AuctionId


class GetAuction:
    def __init__(
        self,
        *,
        user_gateway: IUserGateway,
        auction_gateway: IAuctionGateway,
    ):
        self.user_gateway = user_gateway
        self.auction_gateway = auction_gateway

    async def __call__(self, auction_id: AuctionId) -> AuctionOutput:
        auction = await self.auction_gateway.get_auction_by_id(auction_id)
        if auction is None:
            raise NotFoundError()
        user = await self.user_gateway.get_user_by_id(auction.user_id)
        if user is None:
            raise NotFoundError()
        return map_auction_to_dto(auction, user)
