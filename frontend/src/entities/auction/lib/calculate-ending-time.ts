import {
  differenceInDays,
  differenceInHours,
  differenceInMinutes,
} from 'date-fns'

import { pluralize } from '@/shared/lib'

export const calculateEndingTime = (endingTime: string): string => {
  const auctionEnd = new Date(endingTime)
  const now = new Date()
  const diffInMinutes = differenceInMinutes(auctionEnd, now)
  if (diffInMinutes <= 0) {
    return 'Auction ended'
  }
  const minutes = diffInMinutes % 60
  const hours = differenceInHours(auctionEnd, now) % 24
  const days = differenceInDays(auctionEnd, now)

  if (days > 0) {
    return pluralize(days, 'day', 'days')
  } else if (hours > 0) {
    if (minutes > 0) {
      return `${hours} h ${minutes} m`
    } else {
      return `${hours} h`
    }
  } else if (minutes > 0) {
    return `${minutes} min`
  } else {
    return '<1 min'
  }
}
