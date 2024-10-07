declare global {
  export type Theme = 'light' | 'dark'

  export type Optional<T> = T | null

  export type Keys<T extends Record<string, unknown>> = keyof T

  export type Values<T extends Record<string, unknown>> = T[Keys<T>]

  type RootState = import('../src/app/store').RootState

  type AppDispatch = import('../src/app/store').AppDispatch
}

export {}
