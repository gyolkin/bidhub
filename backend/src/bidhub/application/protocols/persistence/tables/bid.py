from abc import ABC, abstractmethod

from bidhub.application.dto.bid import DetailedBidResponse, ListBidsFilter


class IBidTable(ABC):
    @abstractmethod
    async def list_bids_with_total(self, filters: ListBidsFilter) -> tuple[list[DetailedBidResponse], int]:
        raise NotImplementedError
