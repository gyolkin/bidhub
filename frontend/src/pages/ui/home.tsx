import { AuctionList } from '@/widgets/auction-list'
import { WelcomeSection } from '@/widgets/welcome-section'
import { AuctionSearchForm } from '@/features/auction/search'
import {
  AUCTIONS_PER_PAGE,
  auctionsApi,
  REFETCH_AUCTIONS_INTERVAL,
} from '@/entities/auction'
import { ActionLink } from '@/shared/kit'
import { TypographyH3 } from '@/shared/ui'

const HomePage = () => {
  return (
    <div className="py-10 space-y-4">
      <WelcomeSection />
      <TypographyH3 className="text-center">
        There are <strong>1,000+</strong> auctions for you
      </TypographyH3>
      <LatestAuctionsList />
    </div>
  )
}

const LatestAuctionsList = () => {
  const {
    data: auctions,
    isLoading,
    isError,
  } = auctionsApi.endpoints.listAuctions.useQuery(
    {
      page: 1,
      per_page: AUCTIONS_PER_PAGE,
    },
    {
      pollingInterval: REFETCH_AUCTIONS_INTERVAL,
    }
  )

  return (
    <div className="space-y-2">
      <AuctionSearchForm />
      <AuctionList
        auctions={auctions?.items}
        showSkeleton={isLoading}
        showError={isError}
        loadedAuctions={AUCTIONS_PER_PAGE}
        showAddButton
      />
      <div className="flex justify-center pt-2">
        <ActionLink to="/auctions">All auctions</ActionLink>
      </div>
    </div>
  )
}

export { HomePage }
