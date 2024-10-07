interface PaginationFilter {
  per_page: number
  page: number
}

interface PaginatedResponse<T> {
  items: Array<T>
  total_items: number
  total_pages: number
}

export type { PaginatedResponse, PaginationFilter }
