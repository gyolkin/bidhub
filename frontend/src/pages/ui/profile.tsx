import { useParams } from 'react-router-dom'

import { AuctionList } from '@/widgets/auction-list'
import { auctionsApi } from '@/entities/auction'
import { ProfileCard, ProfileCardSkeleton, usersApi } from '@/entities/user'
import { ActionLink } from '@/shared/kit'
import { createQueryString } from '@/shared/lib'
import { TypographyH3 } from '@/shared/ui'
import { skipToken } from '@reduxjs/toolkit/query'

const AUCTIONS_PER_PROFILE = 4

const ProfilePage = () => {
  const { user_id } = useParams()
  const { data: user, isError: userError } =
    usersApi.endpoints.getUser.useQuery(user_id ? { user_id } : skipToken)

  if (!user_id || userError) {
    throw new Error('Profile Not Found')
  }

  return (
    <div className="pt-10 pb-2 space-y-4">
      {user ? <ProfileCard user={user} /> : <ProfileCardSkeleton />}
      <ProfileAuctionsList />
    </div>
  )
}

const ProfileAuctionsList = () => {
  const { user_id } = useParams()
  const {
    data: auctions,
    isLoading: auctionsLoading,
    isError: auctionsError,
  } = auctionsApi.endpoints.listAuctions.useQuery(
    user_id ? { user_id: user_id, per_page: AUCTIONS_PER_PROFILE } : skipToken
  )

  return (
    <div className="space-y-2 pt-5">
      <div className="flex justify-between gap-4 md:justify-start">
        <TypographyH3>Latest auctions</TypographyH3>
        <ActionLink
          to={{
            pathname: '/auctions',
            search: createQueryString({ user_id }),
          }}
        >
          All auctions
        </ActionLink>
      </div>
      <AuctionList
        auctions={auctions?.items}
        showSkeleton={auctionsLoading}
        showError={auctionsError}
        loadedAuctions={AUCTIONS_PER_PROFILE}
      />
    </div>
  )
}

export { ProfilePage }
