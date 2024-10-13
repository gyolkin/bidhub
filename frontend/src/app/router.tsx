import { createBrowserRouter } from 'react-router-dom'

import {
  AuctionsPage,
  HomePage,
  LoginPage,
  NotFoundPage,
  ProfilePage,
  RegisterPage,
  SingleAuctionPage,
} from '@/pages/ui'

import { baseLayout, emptyLayout } from './layouts/base'
import { ProtectedRoute, PublicRoute } from './route-wrappers'

export const appRouter = () =>
  createBrowserRouter([
    {
      element: emptyLayout,
      errorElement: <NotFoundPage />,
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
    {
      element: baseLayout,
      errorElement: <NotFoundPage />,
      children: [
        {
          path: '/',
          element: <HomePage />,
        },
        {
          path: '/profile/:user_id',
          element: <ProtectedRoute element={<ProfilePage />} />,
        },
        {
          path: '/auctions',
          element: <AuctionsPage />,
        },
        {
          path: '/auction/:auction_id',
          element: <SingleAuctionPage />,
        },
      ],
    },
  ])
