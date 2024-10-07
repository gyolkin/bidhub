import { Link } from 'react-router-dom'

import { cn, pluralize } from '@/shared/lib'
import {
  Card,
  CardContent,
  CardHeader,
  TypographyH3,
  TypographyP,
} from '@/shared/ui'

import { calculateEndingTime } from '../lib'
import type { ShortAuction } from '../model/types'

interface AuctionCardProps {
  auction: ShortAuction
}

export const AuctionCard = ({ auction }: AuctionCardProps) => {
  return (
    <Link to={`/auction/${auction.id}`} className="block">
      <Card className={cn(!auction.is_active && 'opacity-50')}>
        <CardHeader>
          <TypographyH3>{auction.title}</TypographyH3>
          <TypographyP muted>
            {calculateEndingTime(auction.ending_at)}
          </TypographyP>
        </CardHeader>
        <CardContent>
          <TypographyP>
            {pluralize(auction.total_bids, 'bid', 'bids')}
          </TypographyP>
          <TypographyH3>${auction.current_price}</TypographyH3>
        </CardContent>
      </Card>
    </Link>
  )
}
