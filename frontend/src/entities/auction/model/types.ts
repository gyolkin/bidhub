export type AuctionId = string

export interface ShortAuction {
  id: AuctionId
  title: string
  current_price: number
  total_bids: number
  created_at: string
  ending_at: string
  is_active: boolean
}
