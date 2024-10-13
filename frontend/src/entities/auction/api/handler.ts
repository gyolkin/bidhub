import { baseApi, IdResponse } from '@/shared/api'
import type { PaginatedResponse, PaginationFilter } from '@/shared/model'

import { type AuctionId } from '../model'
import type {
  CreateAuctionRequest,
  DetailedAuctionResponse,
  ListAuctionsFilter,
  ShortAuctionResponse,
} from './types'

const AUCTIONS_ENDPOINT = '/auctions'

const auctionsApi = baseApi.injectEndpoints({
  endpoints: (build) => ({
    listAuctions: build.query<
      PaginatedResponse<ShortAuctionResponse>,
      ListAuctionsFilter & PaginationFilter
    >({
      query: (filters) => {
        return {
          url: AUCTIONS_ENDPOINT,
          params: filters,
          method: 'GET',
        }
      },
      providesTags: ['AUCTIONS'],
    }),
    getAuction: build.query<DetailedAuctionResponse, { auction_id: AuctionId }>(
      {
        query: ({ auction_id }) => ({
          url: `${AUCTIONS_ENDPOINT}/${auction_id}`,
          method: 'GET',
        }),
        providesTags: ['AUCTIONS'],
      }
    ),
    createAuction: build.mutation<IdResponse<AuctionId>, CreateAuctionRequest>({
      query: (data) => ({
        url: AUCTIONS_ENDPOINT,
        method: 'POST',
        body: data,
      }),
      invalidatesTags: ['AUCTIONS'],
    }),
  }),
})

export { auctionsApi }
