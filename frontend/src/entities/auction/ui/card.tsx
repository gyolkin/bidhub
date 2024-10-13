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
      <Card
        className={cn(
          'flex flex-col min-h-56 justify-between transition-transform duration-300 hover:scale-105',
          !auction.is_active && 'opacity-50 hover:opacity-100'
        )}
      >
        <CardHeader>
          <TypographyH3 className="title-clamp">{auction.title}</TypographyH3>
          <TypographyP muted>
            {calculateEndingTime(auction.ending_at)}
          </TypographyP>
        </CardHeader>
        <CardContent>
          <TypographyP>
            {pluralize(auction.total_bids, 'bid', 'bids')}
          </TypographyP>
          <TypographyH3 className="text-green-600">
            ${auction.current_price}
          </TypographyH3>
        </CardContent>
      </Card>
    </Link>
  )
}
