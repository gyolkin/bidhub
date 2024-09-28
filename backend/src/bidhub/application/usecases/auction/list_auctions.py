from bidhub.application.dto.auction import ListAuctionsFilter, AuctionOutput, map_auction_to_dto
from bidhub.application.dto.common import PaginatedItemsOutput
from bidhub.application.protocols.persistence import IAuctionGateway, IUserGateway


class ListAuctions:
    def __init__(
        self,
        *,
        auction_gateway: IAuctionGateway,
        user_gateway: IUserGateway,
    ):
        self.auction_gateway = auction_gateway
        self.user_gateway = user_gateway

    async def __call__(self, filters: ListAuctionsFilter) -> PaginatedItemsOutput[AuctionOutput]:
        auctions, total_auctions = await self.auction_gateway.list_auctions(filters)
        users = await self.user_gateway.list_users_by_ids({auction.user_id for auction in auctions})
        user_map = {user.id: user for user in users}
        auction_outputs = [map_auction_to_dto(auction, user_map[auction.user_id]) for auction in auctions]
        total_pages = (total_auctions + filters.per_page - 1) // filters.per_page
        return PaginatedItemsOutput(
            items=auction_outputs,
            total_items=total_auctions,
            total_pages=total_pages,
        )
