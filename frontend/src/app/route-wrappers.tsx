import React from 'react'
import { Navigate } from 'react-router-dom'

import { usersApi } from '@/entities/user'

interface ProtectedRouteProps {
  requiredRole?: 'user' | 'admin'
  element: React.ReactNode
}

interface PublicRouteProps {
  element: React.ReactNode
}

const ProtectedRoute = ({
  requiredRole = 'user',
  element,
}: ProtectedRouteProps) => {
  const { data: user } = usersApi.endpoints.getCurrentUser.useQueryState()

  if (!user) {
    return <Navigate to="/login" replace />
  }

  if (requiredRole === 'admin' && !user.is_admin) {
    return <Navigate to="/" replace />
  }

  return element
}

const PublicRoute = ({ element }: PublicRouteProps) => {
  const { data: user } = usersApi.endpoints.getCurrentUser.useQueryState()

  if (user) {
    return <Navigate to="/" replace />
  }

  return element
}

export { ProtectedRoute, PublicRoute }
