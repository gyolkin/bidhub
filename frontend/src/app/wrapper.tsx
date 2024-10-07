import React from 'react'

import { usersApi } from '@/entities/user'
import { FlexCentred } from '@/shared/ui'

const InitializationWrapper = ({ children }: React.PropsWithChildren) => {
  const { isLoading } = usersApi.endpoints.getCurrentUser.useQuery()

  if (isLoading) return <FlexCentred>Loading...</FlexCentred>

  return children
}

export { InitializationWrapper }
