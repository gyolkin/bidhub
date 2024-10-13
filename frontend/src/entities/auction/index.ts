export {
  auctionsApi,
  type DetailedAuctionResponse,
  type ShortAuctionResponse,
} from './api'
export { calculateEndingTime, mapShortAuction } from './lib'
export {
  type AuctionId,
  auctionId,
  AUCTIONS_PER_PAGE,
  auctionTitle,
  isAuctionActive,
  REFETCH_AUCTIONS_INTERVAL,
} from './model'
export { AlertWinner, AuctionCard, AuctionCardSkeleton } from './ui'
