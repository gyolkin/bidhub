from sqlalchemy import Select

from bidhub.application.dto.common import PaginationFilter


def apply_pagination(query: Select, pagination_filter: PaginationFilter) -> Select:
    page = pagination_filter.page
    per_page = pagination_filter.per_page
    offset = (page - 1) * per_page
    return query.offset(offset).limit(per_page)
