import type { ShortAuctionResponse } from '../api/types'
import type { ShortAuction } from '../model/types'

export const mapShortAuction = (dto: ShortAuctionResponse): ShortAuction => {
  return {
    id: dto.id,
    user_id: dto.user_id,
    title: dto.title,
    total_bids: dto.total_bids,
    current_price:
      dto.highest_bid_amount === 0 ? dto.start_price : dto.highest_bid_amount,
    created_at: dto.created_at,
    ending_at: dto.ending_at,
    is_active: dto.is_active,
  }
}
