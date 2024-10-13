import { LogOut } from 'lucide-react'

import { usersApi } from '@/entities/user'
import { baseApi } from '@/shared/api'
import { useAppDispatch } from '@/shared/lib'
import { Button, DropdownMenuItem } from '@/shared/ui'

interface LogoutButtonProps {
  display: 'button' | 'dropdown'
}

const LogoutButton = ({ display }: LogoutButtonProps) => {
  const dispatch = useAppDispatch()
  const [trigger] = usersApi.endpoints.logoutUser.useMutation()
  const handleLogout = async () => {
    await trigger().unwrap()
    dispatch(baseApi.util.resetApiState())
  }
  if (display === 'dropdown') {
    return (
      <DropdownMenuItem onClick={handleLogout}>
        <LogOut className="mr-2 h-4 w-4" />
        <span>Sign Out</span>
      </DropdownMenuItem>
    )
  }
  return (
    <Button variant="destructive">
      <LogOut className="mr-2 h-4 w-4" />
      <span>Sign Out</span>
    </Button>
  )
}

export { LogoutButton }
