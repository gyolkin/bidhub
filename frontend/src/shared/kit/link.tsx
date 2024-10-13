import { ArrowRight } from 'lucide-react'
import { Link, LinkProps } from 'react-router-dom'

import { Button } from '../ui'

interface ActionLinkProps extends LinkProps, React.PropsWithChildren {}

export const ActionLink = ({ children, ...props }: ActionLinkProps) => {
  return (
    <Button asChild variant="link" size="link">
      <Link {...props}>
        <span>{children}</span>
        <ArrowRight className="h-4 w-4" />
      </Link>
    </Button>
  )
}
