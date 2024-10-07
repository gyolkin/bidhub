import { Search } from 'lucide-react'
import { useForm } from 'react-hook-form'
import { useNavigate, useSearchParams } from 'react-router-dom'
import { z } from 'zod'

import { parseAuctionQueryParams } from '@/entities/auction'
import { buildQueryParams } from '@/shared/lib'
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

import { searchFormSchema } from '../model'

export const AuctionSearchForm = () => {
  const [URLSearchParams] = useSearchParams()
  const navigate = useNavigate()
  const form = useForm<z.infer<typeof searchFormSchema>>({
    resolver: zodResolver(searchFormSchema),
    defaultValues: {
      is_active: null,
      ...parseAuctionQueryParams(URLSearchParams),
    },
  })

  return (
    <Form {...form}>
      <form
        className="w-full inline-flex items-center gap-2 lg:gap-4"
        onSubmit={form.handleSubmit((values) =>
          navigate({ pathname: '/auctions', search: buildQueryParams(values) })
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
                  onValueChange={(value) => {
                    field.onChange(value === 'all' ? null : value === 'active')
                  }}
                  value={
                    field.value === null
                      ? 'all'
                      : field.value === true
                        ? 'active'
                        : 'inactive'
                  }
                  defaultValue="all"
                >
                  <SelectTrigger>
                    <SelectValue>
                      {field.value === null
                        ? 'All'
                        : field.value === true
                          ? 'Active'
                          : 'Inactive'}
                    </SelectValue>
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="all">
                      Show <strong>all</strong> auctions
                    </SelectItem>
                    <SelectItem value="active">
                      Show only <strong>active</strong> auctions
                    </SelectItem>
                    <SelectItem value="inactive">
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
