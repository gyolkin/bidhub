export type UserId = string

export interface User {
  id: UserId
  email: string
  password: string
  is_admin: boolean
  created_at: string
}

export interface SafeUser extends Omit<User, 'password'> {}
