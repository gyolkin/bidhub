import { z } from 'zod'

export const searchFormSchema = z.object({
  title: z.string().trim().min(1).optional(),
  is_active: z.boolean().nullable(),
})
