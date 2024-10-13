import { CalendarDays } from 'lucide-react'

import { getShortDate } from '../lib'

interface ShortDateProps {
  date: string
  prefix?: string
}

const ShortDate = ({ date, prefix }: ShortDateProps) => {
  return (
    <div className="flex items-center pt-2">
      <CalendarDays className="mr-2 h-4 w-4 opacity-70" />
      <span className="text-xs text-muted-foreground">
        {prefix ?? ''} {getShortDate(date)}
      </span>
    </div>
  )
}

export { ShortDate }
