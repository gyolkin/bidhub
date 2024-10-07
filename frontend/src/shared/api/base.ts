import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

export const baseApi = createApi({
  reducerPath: 'baseApi',
  baseQuery: fetchBaseQuery({
    baseUrl: 'http://localhost/api/v1',
  }),
  endpoints: () => ({}),
  tagTypes: ['USERS', 'CURRENT_USER'],
})
