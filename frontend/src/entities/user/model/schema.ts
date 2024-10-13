import { z } from 'zod'

const userId = z.string().uuid().optional()

export { userId }
