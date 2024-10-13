import { z } from 'zod'

export const priceSchema = z
  .string()
  .transform((val) => parseFloat(val))
  .refine((value) => !isNaN(value), { message: 'Enter a valid number.' })
  .refine((value) => value > 0, { message: 'Price cannot be negative.' })
