import { z } from 'zod'

import { auctionTitle } from '@/entities/auction'
import { priceSchema } from '@/shared/model'

export const addAuctionFormSchema = z.object({
  title: auctionTitle,
  description: z
    .string()
    .min(1, { message: 'Description is required and cannot be empty.' }),
  start_price: priceSchema,
  mins_to_finish: z
    .number()
    .min(60, { message: 'Auction duration must be at least 60 minutes.' })
    .max(525_600, { message: 'Auction duration cannot exceed 1 year.' }),
})
