import type { BidResponse } from '../api/types'
import type { Bid } from '../model/types'

export const mapBid = (dto: BidResponse): Bid => {
  return {
    id: dto.id,
    amount: dto.amount,
    created_at: dto.created_at,
  }
}
