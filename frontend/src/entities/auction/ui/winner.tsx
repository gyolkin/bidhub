import { Crown } from "lucide-react"

import { Alert, AlertDescription,AlertTitle } from "@/shared/ui"

interface AlertWinnerProps {
  userSlot: React.ReactNode
}

const AlertWinner = ({ userSlot }: AlertWinnerProps) => {
  return (
    <Alert variant='default'>
        <Crown className="h-4 w-4" />
        <AlertTitle>We have a winner!</AlertTitle>
      <AlertDescription>{userSlot} takes the crown with the highest bid!</AlertDescription>
    </Alert>
  )
}

export { AlertWinner }
