import { createSlice, type PayloadAction } from '@reduxjs/toolkit'

import { getInitialTheme } from '../lib/get-initial-theme'

type ThemeSliceState = {
  appTheme: Theme
}

const initialState: ThemeSliceState = {
  appTheme: getInitialTheme(),
}

export const themeSlice = createSlice({
  name: 'theme',
  initialState,
  reducers: {
    setTheme: (state, action: PayloadAction<Theme>) => {
      state.appTheme = action.payload
    },
  },
})

export const selectAppTheme = (state: RootState) => state.theme.appTheme
export const { setTheme } = themeSlice.actions
