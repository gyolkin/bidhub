import type { SafeUser, User } from '../model'

export type UserResponse = SafeUser
export type UserIdResponse = Pick<SafeUser, 'id'>
export type UserLoginRequest = Pick<User, 'email' | 'password'>
export type UserRegisterRequest = UserLoginRequest
