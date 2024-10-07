import type { ListAuctionsFilter } from '../api/types'

export const parseAuctionQueryParams = (
  query: URLSearchParams
): ListAuctionsFilter => {
  const result: ListAuctionsFilter = {}
  const is_active = query.get('is_active')
  const title = query.get('title')
  if (is_active) {
    result.is_active = is_active === 'false' ? false : true
  }
  if (title) {
    result.title = title
  }
  return result
}
