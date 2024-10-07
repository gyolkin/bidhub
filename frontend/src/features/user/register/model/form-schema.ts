import { z } from 'zod'

export const registerFormSchema = z.object({
  email: z
    .string()
    .min(1, { message: 'This field has to be filled.' })
    .email('This is not a valid email.'),
  password: z
    .string()
    .min(8, { message: 'This field has to be at least 8 digits length.' }),
})
