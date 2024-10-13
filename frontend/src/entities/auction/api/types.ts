import type { BidId } from '@/entities/bid/@x/auction'
import type { UserId, UserResponse } from '@/entities/user/@x/auction'

import type { AuctionId } from '../model'

interface AuctionHighestBidResponse {
  id: BidId
  user: UserResponse
  amount: number
  created_at: string
}

interface DetailedAuctionResponse {
  id: AuctionId
  user: UserResponse
  title: string
  description: string
  start_price: number
  created_at: string
  ending_at: string
  is_active: boolean
  total_bids: number
  highest_bid: Optional<AuctionHighestBidResponse>
}

interface ShortAuctionResponse {
  id: AuctionId
  user_id: UserId
  highest_bid_amount: number
  total_bids: number
  title: string
  start_price: number
  created_at: string
  ending_at: string
  is_active: boolean
}

interface CreateAuctionRequest {
  title: string
  description: string
  start_price: number
  mins_to_finish: number
}

interface ListAuctionsFilter {
  user_id?: UserId
  title?: string
  is_active?: string
}

export type {
  CreateAuctionRequest,
  DetailedAuctionResponse,
  ListAuctionsFilter,
  ShortAuctionResponse,
}
