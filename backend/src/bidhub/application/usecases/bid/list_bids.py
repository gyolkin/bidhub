from bidhub.application.dto.bid import ListBidsFilter, BidOutput, map_auction_bids_to_dto
from bidhub.application.dto.common import PaginatedItemsOutput
from bidhub.application.protocols.persistence import IBidGateway, IAuctionGateway, IUserGateway


class ListBids:
    def __init__(
        self,
        *,
        bid_gateway: IBidGateway,
        auction_gateway: IAuctionGateway,
        user_gateway: IUserGateway,
    ):
        self.bid_gateway = bid_gateway
        self.auction_gateway = auction_gateway
        self.user_gateway = user_gateway

    async def __call__(self, filters: ListBidsFilter) -> PaginatedItemsOutput[BidOutput]:
        bids, total_bids = await self.bid_gateway.list_bids(filters)
        users = await self.user_gateway.list_users_by_ids({bid.user_id for bid in bids})
        user_map = {user.id: user for user in users}
        bid_outputs = [map_auction_bids_to_dto(bid, user_map[bid.user_id]) for bid in bids]
        total_pages = (total_bids + filters.per_page - 1) // filters.per_page
        return PaginatedItemsOutput(
            items=bid_outputs,
            total_items=total_bids,
            total_pages=total_pages,
        )
