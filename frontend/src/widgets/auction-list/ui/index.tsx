import { AddAuctionDialog } from '@/features/auction/add'
import {
  AuctionCard,
  AuctionCardSkeleton,
  mapShortAuction,
  type ShortAuctionResponse,
} from '@/entities/auction'
import { TypographyH3 } from '@/shared/ui'

interface AuctionListProps {
  auctions?: Array<ShortAuctionResponse>
  showSkeleton: boolean
  showError: boolean
  loadedAuctions: number
  showAddButton?: boolean
}

const AuctionList = ({
  auctions,
  showSkeleton,
  showError,
  loadedAuctions,
  showAddButton,
}: AuctionListProps) => {
  const renderAuctions = () => {
    if (showSkeleton) {
      return Array.from({ length: loadedAuctions }).map((_, index) => (
        <AuctionCardSkeleton key={index} />
      ))
    } else {
      return auctions?.map((auction) => (
        <AuctionCard key={auction.id} auction={mapShortAuction(auction)} />
      ))
    }
  }

  if (showError || auctions?.length === 0) {
    return (
      <div className="block text-center space-y-4">
        <TypographyH3>Auctions not found</TypographyH3>
        {showAddButton && <AddAuctionDialog type="button" />}
      </div>
    )
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      {showAddButton && <AddAuctionDialog type="card" />}
      {renderAuctions()}
    </div>
  )
}

export { AuctionList }
