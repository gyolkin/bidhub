import { AuctionId } from '@/entities/auction/@x/bid'
import type { UserId, UserResponse } from '@/entities/user/@x/bid'

import type { BidId } from '../model'

interface BidAuctionResponse {
  id: AuctionId
  title: string
  is_active: boolean
}

interface BidResponse {
  id: BidId
  user: UserResponse
  auction: BidAuctionResponse
  amount: number
  created_at: string
}

interface CreateBidRequest {
  body: {
    amount: number
  }
  params: {
    auction_id: AuctionId
  }
}

interface ListBidsFilter {
  user_id?: UserId
  auction_id?: AuctionId
}

export type { BidResponse, CreateBidRequest, ListBidsFilter }
