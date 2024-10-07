import { Card, CardContent, CardHeader, Skeleton } from '@/shared/ui'

export const AuctionCardSkeleton = () => {
  return (
    <Card>
      <CardHeader>
        <Skeleton className="h-6 w-3/4" />
        <Skeleton className="h-4 w-1/2" />
      </CardHeader>
      <CardContent>
        <Skeleton className="h-4 w-1/4" />
        <Skeleton className="h-6 w-1/4" />
      </CardContent>
    </Card>
  )
}
