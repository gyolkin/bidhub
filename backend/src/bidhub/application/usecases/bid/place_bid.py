from bidhub.application.exceptions import NotFoundError
from bidhub.application.dto.bid import CreateBidRequest
from bidhub.application.dto.common import IdResponse
from bidhub.application.protocols.security import IUserIdentity
from bidhub.application.protocols.persistence import IBidGateway, IAuctionGateway, IUnitOfWork
from bidhub.core.services import BidService
from bidhub.core.models import AuctionId, BidId


AUCTION_NOT_FOUND = 'Auction does not exist.'


class PlaceBid:
    def __init__(
        self,
        *,
        user_identity: IUserIdentity,
        bid_service: BidService,
        bid_gateway: IBidGateway,
        auction_gateway: IAuctionGateway,
        uow: IUnitOfWork,
    ):
        self.user_identity = user_identity
        self.bid_service = bid_service
        self.bid_gateway = bid_gateway
        self.auction_gateway = auction_gateway
        self.uow = uow

    async def __call__(self, auction_id: AuctionId, request: CreateBidRequest) -> IdResponse[BidId]:
        current_user = await self.user_identity.get_current_user()
        auction = await self.auction_gateway.get_auction_by_id(auction_id)
        if not auction:
            raise NotFoundError(AUCTION_NOT_FOUND)
        new_bid = self.bid_service.create_bid(
            auction_id=auction.id,
            user_id=current_user.id,
            amount=request.amount,
        )
        await self.bid_gateway.save_bid(new_bid)
        await self.uow.commit()
        return IdResponse(new_bid.id)
