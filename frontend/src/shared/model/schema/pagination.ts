import { z } from 'zod'

export const paginationSchema = z.object({
  page: z
    .preprocess((val) => {
      const parsed = parseInt(val as string, 10)
      return isNaN(parsed) ? undefined : parsed
    }, z.number().int().positive())
    .optional()
    .default(1),
  per_page: z
    .preprocess((val) => {
      const parsed = parseInt(val as string, 10)
      return isNaN(parsed) ? undefined : parsed
    }, z.number().int().positive())
    .optional()
    .default(10),
})
