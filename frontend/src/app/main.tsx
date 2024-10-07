import React from 'react'
import ReactDOM from 'react-dom/client'
import { Provider as ReduxProvider } from 'react-redux'
import { RouterProvider } from 'react-router-dom'

import { ThemeProvider } from '@/entities/theme'

import { appRouter } from './router'
import { store } from './store'
import { InitializationWrapper } from './wrapper'

import '@/shared/index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <ReduxProvider store={store}>
      <ThemeProvider>
        <InitializationWrapper>
          <RouterProvider router={appRouter()} />
        </InitializationWrapper>
      </ThemeProvider>
    </ReduxProvider>
  </React.StrictMode>
)
