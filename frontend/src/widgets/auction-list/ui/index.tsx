import { AddAuctionDialog } from '@/features/auction/add'
import {
  AuctionCard,
  AuctionCardSkeleton,
  AUCTIONS_PER_PAGE,
  auctionsApi,
  mapShortAuction,
  REFETCH_AUCTIONS_INTERVAL,
} from '@/entities/auction'

const AuctionList = () => {
  const { data: auctions, isLoading } =
    auctionsApi.endpoints.listAuctions.useQuery(
      {
        page: 1,
        per_page: AUCTIONS_PER_PAGE,
      },
      {
        pollingInterval: REFETCH_AUCTIONS_INTERVAL,
      }
    )

  const renderAuctions = () => {
    if (!auctions || isLoading) {
      return Array.from({ length: 40 }).map((_, index) => (
        <AuctionCardSkeleton key={index} />
      ))
    } else {
      return auctions.items.map((auction) => (
        <AuctionCard key={auction.id} auction={mapShortAuction(auction)} />
      ))
    }
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      <AddAuctionDialog type="card" />
      {renderAuctions()}
    </div>
  )
}

export { AuctionList }
