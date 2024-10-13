import React from 'react'

import { getDayWithTime } from '@/shared/lib'
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/shared/ui'

import type { Bid } from '../model'

interface BidRowProps {
  userSlot: React.ReactNode
  bid: Bid
}

const BidTable = ({ children }: React.PropsWithChildren) => {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead className="w-[100px]">User</TableHead>
          <TableHead>Date</TableHead>
          <TableHead>Amount</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>{children}</TableBody>
    </Table>
  )
}

const BidRow = ({ userSlot, bid }: BidRowProps) => {
  return (
    <TableRow>
      <TableCell>{userSlot}</TableCell>
      <TableCell>{getDayWithTime(bid.created_at)}</TableCell>
      <TableCell>${bid.amount}</TableCell>
    </TableRow>
  )
}

export { BidRow, BidTable }
