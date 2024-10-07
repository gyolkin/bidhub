import { Moon, Sun } from 'lucide-react'

import { selectAppTheme, setTheme } from '@/entities/theme'
import { useAppDispatch, useAppSelector } from '@/shared/lib'
import { Button } from '@/shared/ui'

const ThemeSwitcher = () => {
  const appTheme = useAppSelector(selectAppTheme)
  const dispatch = useAppDispatch()

  if (appTheme === 'light')
    return (
      <Button
        variant="ghost"
        size="icon"
        onClick={() => dispatch(setTheme('dark'))}
      >
        <Sun />
      </Button>
    )
  return (
    <Button
      variant="ghost"
      size="icon"
      onClick={() => dispatch(setTheme('light'))}
    >
      <Moon />
    </Button>
  )
}

export { ThemeSwitcher }
