import { baseApi, IdResponse } from '@/shared/api'
import type { PaginatedResponse, PaginationFilter } from '@/shared/model'

import type { AuctionId } from '../model'
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
    }),
    getAuction: build.query<DetailedAuctionResponse, AuctionId>({
      query: (auctionId) => ({
        url: `${AUCTIONS_ENDPOINT}/${auctionId}`,
        method: 'GET',
      }),
    }),
    createAuction: build.mutation<IdResponse<AuctionId>, CreateAuctionRequest>({
      query: (data) => ({
        url: AUCTIONS_ENDPOINT,
        method: 'POST',
        body: data,
      }),
    }),
  }),
})

export { auctionsApi }
