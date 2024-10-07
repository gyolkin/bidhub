import React from 'react'
import { Outlet } from 'react-router-dom'

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
    </div>
  )
}

export { Layout }
