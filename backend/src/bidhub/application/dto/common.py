from typing import Generic, TypeVar
from dataclasses import dataclass


T = TypeVar('T')


def count_total_pages(total_items: int, per_page: int):
    return (total_items + per_page - 1) // per_page


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
class PaginatedItemsResponse(Generic[T]):
    items: list[T]
    total_items: int
    total_pages: int


@dataclass(frozen=True, slots=True)
class IdResponse(Generic[T]):
    id: T
