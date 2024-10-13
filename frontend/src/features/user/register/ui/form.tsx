import { useForm } from 'react-hook-form'
import { useNavigate } from 'react-router-dom'
import { z } from 'zod'

import { usersApi } from '@/entities/user'
import { getErrorMessage } from '@/shared/api'
import { AlertDestructive } from '@/shared/kit'
import {
  Button,
  Form,
  FormContainer,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
  Input,
} from '@/shared/ui'
import { zodResolver } from '@hookform/resolvers/zod'

import { registerFormSchema } from '../model'

export const RegisterForm = () => {
  const navigate = useNavigate()
  const [trigger, { isLoading, error }] =
    usersApi.endpoints.registerUser.useMutation()
  const form = useForm<z.infer<typeof registerFormSchema>>({
    resolver: zodResolver(registerFormSchema),
    defaultValues: {
      email: '',
      password: '',
    },
    disabled: isLoading,
  })
  const handleRegister = async (values: z.infer<typeof registerFormSchema>) => {
    await trigger(values).unwrap()
    navigate('/login')
  }

  return (
    <Form {...form}>
      <FormContainer onSubmit={form.handleSubmit(handleRegister)}>
        {error && (
          <AlertDestructive title="Registration Error">
            {getErrorMessage(error)}
          </AlertDestructive>
        )}
        <FormField
          control={form.control}
          name="email"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Email</FormLabel>
              <FormControl>
                <Input placeholder="your@email.com" {...field} type="email" />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="password"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Password</FormLabel>
              <FormControl>
                <Input
                  placeholder="Enter your password"
                  {...field}
                  type="password"
                />
              </FormControl>
              <FormDescription>
                Your password must be strong: at least 8 digits length, contain
                at least one letter and one number.
              </FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />
        <Button type="submit" expand pulse={isLoading} disabled={isLoading}>
          {isLoading ? 'Signing up...' : 'Sign up'}
        </Button>
      </FormContainer>
    </Form>
  )
}
