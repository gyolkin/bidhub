import { getShortDate } from '@/shared/lib'
import {
  Badge,
  Card,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/shared/ui'

import type { SafeUser } from '../model'

interface ProfileCardProps {
  user: SafeUser
}

const ProfileCard = ({ user }: ProfileCardProps) => {
  return (
    <Card className="border-none">
      <CardHeader className="p-0">
        <div className="flex items-center gap-2">
          <CardTitle>{user.email}</CardTitle>
          <Badge>{user.is_admin ? 'Admin' : 'User'}</Badge>
        </div>
        <CardDescription className="max-w-lg text-balance leading-relaxed pt-4">
          Joined {getShortDate(user.created_at)}
        </CardDescription>
      </CardHeader>
    </Card>
  )
}

export { ProfileCard }
