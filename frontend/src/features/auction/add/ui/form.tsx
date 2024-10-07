import { useForm } from 'react-hook-form'
import { useNavigate } from 'react-router-dom'
import { z } from 'zod'

import { auctionsApi } from '@/entities/auction'
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

import { addAuctionFormSchema } from '../model'

export const AddAuctionForm = () => {
  const navigate = useNavigate()
  const [trigger, { isLoading, error }] =
    auctionsApi.endpoints.createAuction.useMutation()
  const form = useForm<z.infer<typeof addAuctionFormSchema>>({
    resolver: zodResolver(addAuctionFormSchema),
    disabled: isLoading,
  })
  const handleCreation = async (
    values: z.infer<typeof addAuctionFormSchema>
  ) => {
    const response = await trigger(values).unwrap()
    navigate(`/auction/${response.id}`)
  }

  return (
    <Form {...form}>
      <FormContainer onSubmit={form.handleSubmit(handleCreation)}>
        {error && (
          <AlertDestructive title="Publishing Error">
            {getErrorMessage(error)}
          </AlertDestructive>
        )}
        <FormField
          control={form.control}
          name="title"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Title</FormLabel>
              <FormControl>
                <Input placeholder="Marvel..." {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="description"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Description</FormLabel>
              <FormControl>
                <Input placeholder="Marvel.." {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="start_price"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Start Price</FormLabel>
              <FormControl>
                <Input
                  placeholder="100"
                  {...field}
                  type="number"
                  onChange={(e) => field.onChange(parseInt(e.target.value))}
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="mins_to_finish"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Minutes to Finish</FormLabel>
              <FormControl>
                <Input
                  placeholder="60"
                  {...field}
                  type="number"
                  onChange={(e) => field.onChange(parseInt(e.target.value))}
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <Button type="submit" expand pulse={isLoading} disabled={isLoading}>
          {isLoading ? 'Publishing...' : 'Publish'}
        </Button>
      </FormContainer>
    </Form>
  )
}
