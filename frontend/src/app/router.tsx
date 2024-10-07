import { createBrowserRouter } from 'react-router-dom'

import {
  AuctionsPage,
  HomePage,
  LoginPage,
  ProfilePage,
  RegisterPage,
} from '@/pages/ui'

import { baseLayout, emptyLayout } from './layouts/base'
import { ProtectedRoute, PublicRoute } from './route-wrappers'

export const appRouter = () =>
  createBrowserRouter([
    {
      element: baseLayout,
      errorElement: <div>error</div>,
      children: [
        {
          path: '/',
          element: <HomePage />,
        },
        {
          path: '/profile',
          element: <ProtectedRoute element={<ProfilePage />} />,
        },
        {
          path: '/auctions',
          element: <AuctionsPage />,
        },
      ],
    },
    {
      element: emptyLayout,
      errorElement: <div>error</div>,
      children: [
        {
          path: '/login',
          element: <PublicRoute element={<LoginPage />} />,
        },
        {
          path: '/register',
          element: <PublicRoute element={<RegisterPage />} />,
        },
      ],
    },
  ])
