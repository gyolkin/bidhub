import { usersApi } from '@/entities/user'

const ProfilePage = () => {
  const { data: user } = usersApi.endpoints.getCurrentUser.useQueryState()
  return (
    <div className="pt-10">
      <p>{user?.email}</p>
    </div>
  )
}

export { ProfilePage }
