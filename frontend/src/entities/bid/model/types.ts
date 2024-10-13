export type BidId = string

export interface Bid {
  id: BidId
  amount: number
  created_at: string
}
