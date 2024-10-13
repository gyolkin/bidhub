import { ActionLink, ShortDate } from '@/shared/kit'
import {
  Button,
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from '@/shared/ui'

import type { SafeUser } from '../model'

interface ProfileHoverCardProps {
  user: SafeUser
}

const ProfileHoverCard = ({ user }: ProfileHoverCardProps) => {
  return (
    <HoverCard>
      <HoverCardTrigger asChild>
        <Button variant="link" size="link">
          {user.email}
        </Button>
      </HoverCardTrigger>
      <HoverCardContent className="w-80">
        <div className="space-y-1">
          <p className="text-sm">{user.email}</p>
          <ShortDate prefix="Joined" date={user.created_at} />
          <ActionLink to={`/profile/${user.id}`}>View profile</ActionLink>
        </div>
      </HoverCardContent>
    </HoverCard>
  )
}

export { ProfileHoverCard }
