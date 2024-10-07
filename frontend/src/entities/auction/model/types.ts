import type { UUID } from 'crypto'

import type { UserId } from '@/entities/user/@x/auction'

export type AuctionId = UUID

export interface Auction {
  id: AuctionId
  user_id: UserId
  title: string
  description: string
  start_price: number
  created_at: string
  ending_at: string
  is_active: boolean
}

export interface ShortAuction {
  id: AuctionId
  user_id: UserId
  title: string
  current_price: number
  total_bids: number
  created_at: string
  ending_at: string
  is_active: boolean
}
