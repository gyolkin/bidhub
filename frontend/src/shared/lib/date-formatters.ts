import { format, parseISO } from 'date-fns'

const formatDate = (date: string, pattern: string): string => {
  return format(parseISO(date), pattern)
}

const getShortDate = (date: string): string => {
  return formatDate(date, 'MMMM yyyy')
}

const getDetailedDate = (date: string): string => {
  return formatDate(date, 'dd MMM yyyy, HH:mm zzz')
}

const getDayWithTime = (date: string): string => {
  return formatDate(date, 'dd MMM, HH:mm')
}

export { getDayWithTime, getDetailedDate, getShortDate }
