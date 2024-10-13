import { Link } from 'react-router-dom'

import { TypographyH2 } from '@/shared/ui'

interface LogoProps {
  navigateOnClick?: boolean
}

const Logo = ({ navigateOnClick }: LogoProps) => {
  const renderLogo = () => (
    <TypographyH2>
      BidHub<strong className="text-primary">.</strong>
    </TypographyH2>
  )

  if (navigateOnClick) {
    return <Link to="/">{renderLogo()}</Link>
  }
  return renderLogo()
}

export { Logo }
