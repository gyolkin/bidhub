from fastapi import Query

from bidhub.application.dto.common import PaginationFilter


async def get_pagination(page: int = Query(1, gt=0), per_page: int = Query(10, gt=0)):
    return PaginationFilter(page, per_page)
