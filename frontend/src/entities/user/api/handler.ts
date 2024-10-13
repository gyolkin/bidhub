import { baseApi } from '@/shared/api'

import type { UserId } from '../model'
import type {
  UserIdResponse,
  UserLoginRequest,
  UserRegisterRequest,
  UserResponse,
} from './types'

const USERS_ENDPOINT = '/users'
const AUTH_ENDPOINT = '/auth'

const usersApi = baseApi.injectEndpoints({
  endpoints: (build) => ({
    getCurrentUser: build.query<UserResponse, void>({
      query: () => ({
        url: USERS_ENDPOINT + '/me',
        method: 'GET',
      }),
      providesTags: ['CURRENT_USER'],
      keepUnusedDataFor: Infinity,
    }),
    getUser: build.query<UserResponse, { user_id: UserId }>({
      query: ({ user_id }) => ({
        url: `${USERS_ENDPOINT}/${user_id}`,
        method: 'GET',
      }),
    }),
    loginUser: build.mutation<UserIdResponse, UserLoginRequest>({
      query: (data) => ({
        url: AUTH_ENDPOINT + '/login',
        method: 'POST',
        body: data,
      }),
      invalidatesTags: ['CURRENT_USER'],
    }),
    registerUser: build.mutation<UserIdResponse, UserRegisterRequest>({
      query: (data) => ({
        url: AUTH_ENDPOINT + '/register',
        method: 'POST',
        body: data,
      }),
    }),
    logoutUser: build.mutation<void, void>({
      query: () => ({
        url: AUTH_ENDPOINT + '/logout',
        method: 'POST',
      }),
      invalidatesTags: ['CURRENT_USER'],
    }),
  }),
})

export { usersApi }
