import { X } from 'lucide-react'

import {
  ProfileHoverCard,
  ProfileHoverCardSkeleton,
  usersApi,
} from '@/entities/user'
import { useQueryParams } from '@/shared/lib'
import { Button, TypographyP } from '@/shared/ui'
import { skipToken } from '@reduxjs/toolkit/query'

import { auctionQuerySchema } from '../model'

export const AuctionSearchUserContext = () => {
  const { queryParams, setQueryParams } = useQueryParams(auctionQuerySchema)
  const {
    data: user,
    isLoading: userLoading,
    isError: userError,
  } = usersApi.endpoints.getUser.useQuery(
    queryParams.user_id ? { user_id: queryParams.user_id } : skipToken
  )

  if (!queryParams.user_id) return null

  // Invalidates 'user_id' param if wrong ID provided or user does not exist
  if (userError) {
    setQueryParams({ user_id: undefined }, { resetPages: true })
    return null
  }

  return (
    <div className="flex flex-nowrap items-center py-2">
      <TypographyP className="text-sm mr-2">Auctions by</TypographyP>
      {!user || userLoading ? (
        <ProfileHoverCardSkeleton />
      ) : (
        <ProfileHoverCard user={user} />
      )}
      <Button
        className="icon"
        variant="ghost"
        onClick={() =>
          setQueryParams({ user_id: undefined }, { resetPages: true })
        }
      >
        <X className="h-4 w-4" />
      </Button>
    </div>
  )
}
