import { pluralize } from '@/shared/lib'

import type { Auction } from '../model/types'

export const calculateEndingTime = (
  endingTime: Auction['ending_at']
): string => {
  const now = new Date()
  const nowUTC = new Date(now.getTime() + now.getTimezoneOffset() * 60000)
  const auctionEnd = new Date(endingTime)
  const diffInMs = auctionEnd.getTime() - nowUTC.getTime()

  if (diffInMs <= 0) {
    return 'Auction ended'
  }

  const diffInMinutes = Math.floor(diffInMs / (1000 * 60))
  const minutes = diffInMinutes % 60
  const hours = Math.floor((diffInMinutes / 60) % 24)
  const days = Math.floor(diffInMinutes / (60 * 24))

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
