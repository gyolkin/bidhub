export const buildQueryParams = (params: Record<string, unknown>): string => {
  return Object.entries(params)
    .filter(([, value]) => value !== null && value !== undefined)
    .map(
      ([key, value]) =>
        `${encodeURIComponent(key)}=${encodeURIComponent(String(value))}`
    )
    .join('&')
}
