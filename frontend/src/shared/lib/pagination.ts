import type { PaginationFilter } from '../model'

export const parsePaginationQueryParams = (
  params: URLSearchParams
): PaginationFilter => {
  const page = parseInt(params.get('page') || '1')
  const result: PaginationFilter = {
    page: page > 0 ? page : 1,
    per_page: 10,
  }
  return result
}
