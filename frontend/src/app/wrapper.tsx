import React from 'react'

import { Logo } from '@/entities/brand'
import { usersApi } from '@/entities/user'
import { FlexCentred, TypographyP } from '@/shared/ui'

const InitializationWrapper = ({ children }: React.PropsWithChildren) => {
  const { isLoading } = usersApi.endpoints.getCurrentUser.useQuery()

  if (isLoading)
    return (
      <FlexCentred className="animate-pulse gap-2">
        <Logo />
        <TypographyP>Loading...</TypographyP>
      </FlexCentred>
    )

  return children
}

export { InitializationWrapper }
