import { Card, CardHeader, Skeleton } from '@/shared/ui'

export const ProfileCardSkeleton = () => {
  return (
    <Card className="border-none">
      <CardHeader className="p-0">
        <Skeleton className="h-8 w-36 mb-2" />
        <Skeleton className="h-5 w-20" />
      </CardHeader>
    </Card>
  )
}
