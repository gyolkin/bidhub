import qs from 'qs'
import { useMemo } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { z, ZodError, type ZodTypeAny } from 'zod'

interface UseQueryParamsOptions {
  pathname?: string
  replace?: boolean
  resetPages?: boolean
}

interface UseQueryParamsReturn<T> {
  queryParams: T
  setQueryParams: (
    newParams: Partial<T>,
    options?: UseQueryParamsOptions
  ) => void
  errors: ZodError<T> | null
}

const useQueryParams = <T extends ZodTypeAny>(
  schema: T
): UseQueryParamsReturn<z.infer<T>> => {
  const location = useLocation()
  const navigate = useNavigate()

  const queryObj = useMemo(() => {
    return qs.parse(location.search, { ignoreQueryPrefix: true })
  }, [location.search])

  const result = useMemo(() => {
    return schema.safeParse(queryObj)
  }, [queryObj, schema])

  const queryParams = useMemo(() => {
    if (result.success) {
      return result.data
    } else {
      return schema.parse({})
    }
  }, [result, schema])

  const setQueryParams = (
    newParams: Partial<z.infer<T>>,
    options?: UseQueryParamsOptions
  ) => {
    const mergedParams = options?.resetPages
      ? { ...queryObj, page: 1, ...newParams }
      : { ...queryObj, ...newParams }
    Object.keys(mergedParams).forEach((key) => {
      if (
        mergedParams[key] === undefined ||
        mergedParams[key] === null ||
        mergedParams[key] === ''
      ) {
        delete mergedParams[key]
      }
    })
    const search = qs.stringify(mergedParams, {
      addQueryPrefix: true,
      arrayFormat: 'brackets',
    })
    navigate(
      {
        pathname: options?.pathname ? options.pathname : location.pathname,
        search: search,
      },
      options?.replace ? { replace: true } : undefined
    )
  }

  return {
    queryParams,
    setQueryParams,
    errors: result.success ? null : result.error,
  }
}

const createQueryString = (params: object) => {
  return qs.stringify(params, { addQueryPrefix: true, arrayFormat: 'brackets' })
}

export { createQueryString, useQueryParams }
