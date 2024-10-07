import type { SerializedError } from '@reduxjs/toolkit'
import type { FetchBaseQueryError } from '@reduxjs/toolkit/query'

const UNKNOWN_ERROR =
  'There is unknown error. Please reload page and try again.'

export const getErrorMessage = (
  error: FetchBaseQueryError | SerializedError
): string => {
  if ('status' in error) {
    if (typeof error.status === 'number') {
      const errData = error.data as { message?: string }
      return errData?.message || UNKNOWN_ERROR
    } else {
      return error.error || UNKNOWN_ERROR
    }
  } else {
    return error.message || UNKNOWN_ERROR
  }
}
