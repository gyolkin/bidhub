from bidhub.application.dto.auction import ListAuctionsFilter, ShortAuctionResponse
from bidhub.application.dto.common import PaginatedItemsResponse, count_total_pages
from bidhub.application.protocols.persistence import IAuctionTable


class ListAuctions:
    def __init__(
        self,
        *,
        auction_table: IAuctionTable,
    ):
        self.auction_table = auction_table

    async def __call__(self, filters: ListAuctionsFilter) -> PaginatedItemsResponse[ShortAuctionResponse]:
        auctions, total_auctions = await self.auction_table.list_auctions_with_total(filters)
        total_pages = count_total_pages(total_auctions, filters.pagination.per_page)
        return PaginatedItemsResponse(
            items=auctions,
            total_items=total_auctions,
            total_pages=total_pages,
        )
