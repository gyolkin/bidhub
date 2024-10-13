import { useState } from 'react'
import { useParams } from 'react-router-dom'

import { AddBidForm } from '@/features/bid/add'
import {
  AlertWinner,
  auctionsApi,
  calculateEndingTime,
  REFETCH_AUCTIONS_INTERVAL,
} from '@/entities/auction'
import {
  BidRow,
  BidRowSkeleton,
  bidsApi,
  BidTable,
  mapBid,
} from '@/entities/bid'
import { ProfileHoverCard } from '@/entities/user'
import { ControlledPagination, ShortDate } from '@/shared/kit'
import { getDetailedDate } from '@/shared/lib'
import { TypographyH2, TypographyH3, TypographyP } from '@/shared/ui'
import { skipToken } from '@reduxjs/toolkit/query'

const SingleAuctionPage = () => {
  const { auction_id } = useParams()
  const { data: auction, isError: auctionError } =
    auctionsApi.endpoints.getAuction.useQuery(
      auction_id ? { auction_id } : skipToken,
      { pollingInterval: REFETCH_AUCTIONS_INTERVAL }
    )

  if (!auction_id || auctionError) {
    throw new Error('Auction Not Found')
  }

  if (!auction) return <div>Loading...</div>

  return (
    <div className="pt-10 pb-2 space-y-4">
      <div className="grid grid-cols-1 gap-4 md:grid-cols-5 lg:gap-8">
        <div className="md:col-span-3">
          <TypographyH2 className="pb-0">{auction.title}</TypographyH2>
          <div className="flex flex-nowrap items-center">
            <TypographyP className="text-sm mr-2">Published by</TypographyP>
            <ProfileHoverCard user={auction.user} />
          </div>
          <div className="pt-6 pb-4 space-y-2">
            <TypographyH3>Description</TypographyH3>
            <TypographyP>{auction.description}</TypographyP>
          </div>
          <ShortDate prefix="Published" date={auction.created_at} />
        </div>
        <div className="md:col-span-2">
          <div className="flex flex-col lg:flex-row p-6 gap-8 lg:gap-2 bg-secondary rounded-md">
            <div className="flex-1 space-y-1">
              <TypographyP>Highest bid:</TypographyP>
              <TypographyH3>
                {auction.highest_bid
                  ? `$${auction.highest_bid.amount}`
                  : 'No bids'}
              </TypographyH3>
              <TypographyP muted>
                Start price: ${auction.start_price}
              </TypographyP>
            </div>
            <div className="flex-1 space-y-1">
              <TypographyP>Ends in:</TypographyP>
              <TypographyH3>
                {calculateEndingTime(auction.ending_at)}
              </TypographyH3>
              <TypographyP muted>
                {getDetailedDate(auction.ending_at)}
              </TypographyP>
            </div>
          </div>
          {auction.is_active && (
            <AddBidForm
              forAuction={auction.id}
              highestBid={
                auction.highest_bid
                  ? auction.highest_bid.amount
                  : auction.start_price
              }
            />
          )}
          <div className="pt-4 space-y-2">
            {!auction.is_active && auction.highest_bid && 
              <AlertWinner userSlot={<ProfileHoverCard user={auction.highest_bid.user} />} />
            }
            <LatestBids />
          </div>
        </div>
      </div>
    </div>
  )
}

const LatestBids = () => {
  const { auction_id } = useParams() as { auction_id: string }
  const [page, setPage] = useState<number>(1)
  const { data: bids, isLoading: bidsLoading } =
    bidsApi.endpoints.listBids.useQuery({
      auction_id,
      page,
      per_page: 5,
    })
  const renderBidTable = () => {
    if (bidsLoading) {
      return (
        <BidTable>
          {Array.from({ length: 5 }).map((_, index) => (
            <BidRowSkeleton key={index} />
          ))}
        </BidTable>
      )
    } else if (bids?.items.length === 0) {
      return (
        <TypographyP className="text-center" muted>
          No bids yet.
        </TypographyP>
      )
    } else {
      return (
        <BidTable>
          {bids?.items.map((bid) => (
            <BidRow
              key={bid.id}
              bid={mapBid(bid)}
              userSlot={<ProfileHoverCard user={bid.user} />}
            />
          ))}
        </BidTable>
      )
    }
  }

  return (
    <div className="space-y-2">
      {renderBidTable()}
      <ControlledPagination
        count={bids?.total_pages || 0}
        page={page}
        onChange={setPage}
      />
    </div>
  )
}

export { SingleAuctionPage }
