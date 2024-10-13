import { baseApi, IdResponse } from '@/shared/api'
import type { PaginatedResponse, PaginationFilter } from '@/shared/model'

import { type BidId } from '../model'
import type { BidResponse, CreateBidRequest, ListBidsFilter } from './types'

const BIDS_ENDPOINT = '/bids'

const bidsApi = baseApi.injectEndpoints({
  endpoints: (build) => ({
    listBids: build.query<
      PaginatedResponse<BidResponse>,
      ListBidsFilter & PaginationFilter
    >({
      query: (filters) => {
        return {
          url: BIDS_ENDPOINT,
          params: filters,
          method: 'GET',
        }
      },
      providesTags: ['BIDS'],
    }),
    createBid: build.mutation<IdResponse<BidId>, CreateBidRequest>({
      query: ({ body, params }) => ({
        url: BIDS_ENDPOINT,
        method: 'POST',
        body: body,
        params: params,
      }),
      invalidatesTags: ['BIDS'],
    }),
  }),
})

export { bidsApi }
