import { AlertCircle } from 'lucide-react'
import React from 'react'

import { Alert, AlertDescription, AlertTitle } from '../ui'

interface AlertDestructiveProps extends React.PropsWithChildren {
  title: string
}

const AlertDestructive = ({ title, children }: AlertDestructiveProps) => {
  return (
    <Alert variant="destructive">
      {title && (
        <>
          <AlertCircle className="h-4 w-4" />
          <AlertTitle>{title}</AlertTitle>
        </>
      )}
      <AlertDescription>{children}</AlertDescription>
    </Alert>
  )
}

export { AlertDestructive }
