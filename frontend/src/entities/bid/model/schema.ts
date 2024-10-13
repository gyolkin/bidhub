import { z } from 'zod'

const bidId = z.string().uuid().optional()
const bidAmount = z.number().positive().int()

export { bidAmount, bidId }
