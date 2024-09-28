from typing import Generic, TypeVar
from dataclasses import dataclass


T = TypeVar('T')


@dataclass(frozen=True, slots=True)
class PaginationFilter:
    page: int
    per_page: int

    def __post_init__(self):
        if self.page < 1:
            raise ValueError('page must be greater than 0')
        if self.per_page < 1:
            raise ValueError('per_page must be greater than 0')


@dataclass(frozen=True, slots=True)
class PaginatedItemsOutput(Generic[T]):
    items: list[T]
    total_items: int
    total_pages: int
