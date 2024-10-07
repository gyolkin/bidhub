import { themeSlice } from '@/entities/theme'
import { baseApi } from '@/shared/api'
import { configureStore } from '@reduxjs/toolkit'

export const store = configureStore({
  reducer: {
    [baseApi.reducerPath]: baseApi.reducer,
    [themeSlice.name]: themeSlice.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(baseApi.middleware),
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch
