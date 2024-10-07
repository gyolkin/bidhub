import { useSearchParams } from 'react-router-dom'

import { AuctionSearchForm } from '@/features/auction/search'
import {
  AuctionCard,
  AuctionCardSkeleton,
  auctionsApi,
  mapShortAuction,
  parseAuctionQueryParams,
} from '@/entities/auction'
import { parsePaginationQueryParams } from '@/shared/lib'

const AuctionsPage = () => {
  const [URLSearchParams] = useSearchParams()
  const { data: auctions, isLoading } =
    auctionsApi.endpoints.listAuctions.useQuery({
      ...parseAuctionQueryParams(URLSearchParams),
      ...parsePaginationQueryParams(URLSearchParams),
    })

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
    <div className="pt-10 space-y-4">
      <AuctionSearchForm />
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {renderAuctions()}
      </div>
    </div>
  )
}

export { AuctionsPage }
