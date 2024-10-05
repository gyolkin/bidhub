from bidhub.application.dto.bid import ListBidsFilter, DetailedBidResponse
from bidhub.application.dto.common import PaginatedItemsResponse, count_total_pages
from bidhub.application.protocols.persistence import IBidTable


class ListBids:
    def __init__(
        self,
        *,
        bid_table: IBidTable,
    ):
        self.bid_table = bid_table

    async def __call__(self, filters: ListBidsFilter) -> PaginatedItemsResponse[DetailedBidResponse]:
        bids, total_bids = await self.bid_table.list_bids_with_total(filters)
        total_pages = count_total_pages(total_bids, filters.pagination.per_page)
        return PaginatedItemsResponse(
            items=bids,
            total_items=total_bids,
            total_pages=total_pages,
        )
