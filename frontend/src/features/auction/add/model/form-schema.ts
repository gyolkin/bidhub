import { z } from 'zod'

export const addAuctionFormSchema = z.object({
  title: z
    .string()
    .min(1, { message: 'Title is required and cannot be empty.' }),
  description: z
    .string()
    .min(1, { message: 'Description is required and cannot be empty.' }),
  start_price: z
    .number()
    .min(1, { message: 'Start price must be at least 1.' }),
  mins_to_finish: z
    .number()
    .min(60, { message: 'Auction duration must be at least 10 minutes.' })
    .max(525_600, { message: 'Auction duration cannot exceed 1 year.' }),
})
