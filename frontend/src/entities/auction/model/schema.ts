import { z } from 'zod'

const auctionId = z.string().uuid()
const auctionTitle = z
  .string()
  .trim()
  .min(1, { message: 'Title is required and cannot be empty.' })
const isAuctionActive = z.preprocess((value) => {
  if (value === 'true' || value === 'false') return value
  return undefined
}, z.string().optional())

export { auctionId, auctionTitle, isAuctionActive }
