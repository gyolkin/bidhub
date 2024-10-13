import { ActionLink } from '@/shared/kit'
import { FlexCentred, TypographyH2 } from '@/shared/ui'

export const NotFoundPage = () => {
  return (
    <FlexCentred className="gap-2">
      <img
        src="/img/cloud.png"
        alt="cloud"
        className="max-w-xs md:max-w-md lg:max-w-xl"
      />
      <TypographyH2 className="text-center">
        Whoops! That page doesn’t exist.
      </TypographyH2>
      <ActionLink to="/">Homepage</ActionLink>
    </FlexCentred>
  )
}
