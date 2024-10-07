import { Header } from '@/widgets/header'
import { UserMenu } from '@/widgets/usermenu'
import { ThemeSwitcher } from '@/features/theme/switch-theme'
import { Layout } from '@/shared/ui'

export const baseLayout = (
  <Layout
    headerSlot={
      <Header userSlot={<UserMenu />} themeSwitcherSlot={<ThemeSwitcher />} />
    }
  />
)

export const emptyLayout = <Layout />
