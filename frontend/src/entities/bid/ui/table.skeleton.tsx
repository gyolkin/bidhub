import { Skeleton, TableCell, TableRow } from '@/shared/ui'

export const BidRowSkeleton = () => {
  return (
    <TableRow>
      <TableCell>
        <Skeleton className="h-6 w-full" />
      </TableCell>
      <TableCell>
        <Skeleton className="h-6 w-full" />
      </TableCell>
      <TableCell>
        <Skeleton className="h-6 w-full" />
      </TableCell>
    </TableRow>
  )
}
