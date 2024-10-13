import { Search } from 'lucide-react'
import { useForm } from 'react-hook-form'
import { z } from 'zod'

import { useQueryParams } from '@/shared/lib'
import {
  Button,
  Form,
  FormControl,
  FormField,
  FormItem,
  Input,
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/shared/ui'
import { zodResolver } from '@hookform/resolvers/zod'

import { auctionSearchFormSchema } from '../model'

export const AuctionSearchForm = () => {
  const { queryParams, setQueryParams } = useQueryParams(
    auctionSearchFormSchema
  )
  const form = useForm<z.infer<typeof auctionSearchFormSchema>>({
    resolver: zodResolver(auctionSearchFormSchema),
    defaultValues: queryParams,
  })

  return (
    <Form {...form}>
      <form
        className="w-full inline-flex items-center gap-2 lg:gap-4"
        onSubmit={form.handleSubmit((values) =>
          setQueryParams(values, { pathname: '/auctions', resetPages: true })
        )}
      >
        <FormField
          control={form.control}
          name="title"
          render={({ field }) => (
            <FormControl>
              <Input placeholder="What are you interested in?" {...field} />
            </FormControl>
          )}
        />
        <FormField
          control={form.control}
          name="is_active"
          render={({ field }) => (
            <FormItem className="w-48">
              <FormControl>
                <Select
                  onValueChange={field.onChange}
                  value={field.value}
                  defaultValue="all"
                >
                  <SelectTrigger>
                    <SelectValue>
                      {field.value === 'true'
                        ? 'Active'
                        : field.value === 'false'
                          ? 'Inactive'
                          : 'All'}
                    </SelectValue>
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="all">
                      Show <strong>all</strong> auctions
                    </SelectItem>
                    <SelectItem value="true">
                      Show only <strong>active</strong> auctions
                    </SelectItem>
                    <SelectItem value="false">
                      Show only <strong>inactive</strong> auctions
                    </SelectItem>
                  </SelectContent>
                </Select>
              </FormControl>
            </FormItem>
          )}
        />
        <Button type="submit">
          <Search />
          <span className="hidden md:inline">Search</span>
        </Button>
      </form>
    </Form>
  )
}
