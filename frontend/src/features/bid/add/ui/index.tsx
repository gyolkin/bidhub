import { Gavel } from 'lucide-react'
import { useForm } from 'react-hook-form'
import { useNavigate } from 'react-router-dom'
import { z } from 'zod'

import type { AuctionId } from '@/entities/auction'
import { bidsApi } from '@/entities/bid'
import { usersApi } from '@/entities/user'
import { PriceInput } from '@/shared/kit'
import {
  Button,
  Form,
  FormContainer,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/shared/ui'
import { zodResolver } from '@hookform/resolvers/zod'

import { addBidFormSchema } from '../model'

interface AddAuctionFormProps {
  forAuction: AuctionId
  highestBid: number
}

export const AddBidForm = ({ forAuction, highestBid }: AddAuctionFormProps) => {
  const navigate = useNavigate()
  const { data: user } = usersApi.endpoints.getCurrentUser.useQueryState()
  const formSchema = addBidFormSchema(highestBid)
  const [trigger, { isLoading }] = bidsApi.endpoints.createBid.useMutation()
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      amount: Math.ceil(highestBid * 1.05),
    },
    disabled: isLoading,
  })

  const handleCreation = async (values: z.infer<typeof formSchema>) => {
    if (user) {
      await trigger({
        body: values,
        params: { auction_id: forAuction },
      }).unwrap()
    } else {
      navigate('/login')
    }
  }

  return (
    <Form {...form}>
      <FormContainer onSubmit={form.handleSubmit(handleCreation)}>
        <FormField
          control={form.control}
          name="amount"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Your Bid</FormLabel>
              <FormControl>
                <PriceInput {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <Button type="submit" expand pulse={isLoading} disabled={isLoading}>
          <Gavel className="h-4 w-4" />
          <span>{isLoading ? 'Placing your bid...' : 'Place bid'}</span>
        </Button>
      </FormContainer>
    </Form>
  )
}
