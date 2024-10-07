import { LogOut } from 'lucide-react'

import { usersApi } from '@/entities/user'
import { baseApi } from '@/shared/api'
import { useAppDispatch } from '@/shared/lib'
import { DropdownMenuItem } from '@/shared/ui'

const DropdownLogoutButton = () => {
  const dispatch = useAppDispatch()
  const [trigger] = usersApi.endpoints.logoutUser.useMutation()
  const handleLogout = async () => {
    await trigger().unwrap()
    dispatch(baseApi.util.resetApiState())
  }

  return (
    <DropdownMenuItem onClick={handleLogout}>
      <LogOut className="mr-2 h-4 w-4" />
      <span>Sign Out</span>
    </DropdownMenuItem>
  )
}

export { DropdownLogoutButton }
