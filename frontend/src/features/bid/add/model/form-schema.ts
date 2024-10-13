import { z } from 'zod'

import { priceSchema } from '@/shared/model'

export const addBidFormSchema = (highestBid: number) =>
  z.object({
    amount: priceSchema.refine(
      (amount) => {
        return amount > highestBid
      },
      {
        message: `Bid amount must be greater than the current highest bid.`,
      }
    ),
  })
