import { z } from 'zod'

import { auctionTitle, isAuctionActive } from '@/entities/auction'
import { userId } from '@/entities/user'
import { paginationSchema } from '@/shared/model'

export const auctionSearchFormSchema = z.object({
  title: auctionTitle.optional(),
  is_active: isAuctionActive.optional(),
})

export const auctionQuerySchema = auctionSearchFormSchema
  .extend({ user_id: userId })
  .merge(paginationSchema)
