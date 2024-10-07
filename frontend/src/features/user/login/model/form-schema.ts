import { z } from 'zod'

export const loginFormSchema = z.object({
  email: z
    .string()
    .min(1, { message: 'This field has to be filled.' })
    .email('This is not a valid email.'),
  password: z.string().min(1, { message: 'This field has to be filled.' }),
})
