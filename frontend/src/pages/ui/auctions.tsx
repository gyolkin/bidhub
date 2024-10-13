import { AuctionList } from '@/widgets/auction-list'
import {
  auctionQuerySchema,
  AuctionSearchForm,
  AuctionSearchUserContext,
} from '@/features/auction/search'
import {
  AUCTIONS_PER_PAGE,
  auctionsApi,
  REFETCH_AUCTIONS_INTERVAL,
} from '@/entities/auction'
import { ControlledPagination } from '@/shared/kit'
import { useQueryParams } from '@/shared/lib'

const AuctionsPage = () => {
  return (
    <div className="pt-10 pb-2 space-y-4">
      <FullAuctionsList />
    </div>
  )
}

const FullAuctionsList = () => {
  const { queryParams, setQueryParams } = useQueryParams(auctionQuerySchema)
  const {
    data: auctions,
    isLoading: auctionsLoading,
    isError: auctionsError,
  } = auctionsApi.endpoints.listAuctions.useQuery(
    { ...queryParams, per_page: AUCTIONS_PER_PAGE },
    {
      pollingInterval: REFETCH_AUCTIONS_INTERVAL,
    }
  )

  return (
    <>
      <div className="flex flex-col space-y-2 md:flex-col-reverse">
        <AuctionSearchForm />
        <AuctionSearchUserContext />
      </div>
      <AuctionList
        auctions={auctions?.items}
        showSkeleton={auctionsLoading}
        showError={auctionsError}
        loadedAuctions={AUCTIONS_PER_PAGE}
        showAddButton
      />
      <ControlledPagination
        count={auctions?.total_pages || 0}
        page={queryParams.page}
        onChange={(newPage) => setQueryParams({ page: newPage })}
      />
    </>
  )
}

export { AuctionsPage }
