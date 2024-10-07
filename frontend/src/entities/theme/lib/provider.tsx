import { type ReactNode, useEffect } from 'react'

import { useAppSelector } from '@/shared/lib'

import { selectAppTheme } from '../model/slice'

interface ThemeProviderSliceProps {
  children: ReactNode
}

const ThemeProvider = ({ children }: ThemeProviderSliceProps) => {
  const appTheme = useAppSelector(selectAppTheme)

  useEffect(() => {
    const root = window.document.documentElement
    root.classList.remove('dark', 'light')
    root.classList.add(appTheme)
  }, [appTheme])

  return <>{children}</>
}

export { ThemeProvider }
