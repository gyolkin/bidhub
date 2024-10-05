from bidhub.application.exceptions import NotFoundError
from bidhub.application.dto.auction import DetailedAuctionResponse
from bidhub.application.protocols.persistence import IAuctionTable
from bidhub.core.models import AuctionId


class GetAuction:
    def __init__(
        self,
        *,
        auction_table: IAuctionTable,
    ):
        self.auction_table = auction_table

    async def __call__(self, auction_id: AuctionId) -> DetailedAuctionResponse:
        auction = await self.auction_table.get_detailed_auction_by_id(auction_id)
        if auction is None:
            raise NotFoundError()
        return auction
