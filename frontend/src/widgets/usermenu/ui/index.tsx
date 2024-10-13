import { ChevronDown, User } from 'lucide-react'
import { Link } from 'react-router-dom'

import { LogoutButton } from '@/features/user/logout'
import { usersApi } from '@/entities/user'
import {
  Button,
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '@/shared/ui'

const UserMenu = () => {
  const { data: user } = usersApi.endpoints.getCurrentUser.useQueryState()
  if (!user) {
    return (
      <Button asChild>
        <Link to="/login">Sign In</Link>
      </Button>
    )
  }
  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline">
          <ChevronDown className="h-4 w-4" />
          <span>{user.email}</span>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent className="w-56">
        <DropdownMenuGroup>
          <DropdownMenuItem asChild>
            <Link to={`/profile/${user.id}`}>
              <User className="mr-2 h-4 w-4" />
              <span>My Profile</span>
            </Link>
          </DropdownMenuItem>
          <LogoutButton display="dropdown" />
        </DropdownMenuGroup>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}

export { UserMenu }
