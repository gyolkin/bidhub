import { useForm } from 'react-hook-form'
import { z } from 'zod'

import { usersApi } from '@/entities/user'
import { getErrorMessage } from '@/shared/api'
import {
  AlertDestructive,
  Button,
  Form,
  FormContainer,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
  Input,
} from '@/shared/ui'
import { zodResolver } from '@hookform/resolvers/zod'

import { loginFormSchema } from '../model'

export const LoginForm = () => {
  const [trigger, { isLoading, error }] =
    usersApi.endpoints.loginUser.useMutation()
  const form = useForm<z.infer<typeof loginFormSchema>>({
    resolver: zodResolver(loginFormSchema),
    defaultValues: {
      email: '',
      password: '',
    },
    disabled: isLoading,
  })

  return (
    <Form {...form}>
      <FormContainer onSubmit={form.handleSubmit((values) => trigger(values))}>
        {error && (
          <AlertDestructive title="Authentication Error">
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
              <FormMessage />
            </FormItem>
          )}
        />
        <Button type="submit" expand pulse={isLoading} disabled={isLoading}>
          {isLoading ? 'Signing in...' : 'Sign in'}
        </Button>
      </FormContainer>
    </Form>
  )
}
