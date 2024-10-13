import React from 'react'
import { Outlet } from 'react-router-dom'

import { Toaster } from '@/shared/ui'

type LayoutProps = {
  headerSlot?: React.ReactNode
}

const Layout = ({ headerSlot }: LayoutProps) => {
  return (
    <div className="min-h-screen scroll-smooth bg-background">
      {headerSlot}
      <div className="container">
        <Outlet />
      </div>
      <Toaster />
    </div>
  )
}

export { Layout }
