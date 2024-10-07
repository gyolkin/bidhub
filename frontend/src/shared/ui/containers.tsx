import React from 'react'

import { cn } from '../lib'

export interface ContainerProps extends React.HTMLAttributes<HTMLDivElement> {}
export interface FormContainerProps
  extends React.FormHTMLAttributes<HTMLFormElement> {}

const FlexCentred = React.forwardRef<HTMLDivElement, ContainerProps>(
  ({ className, ...props }, ref) => {
    return (
      <div
        className={cn(
          'flex flex-col justify-center items-center py-8 px-6 mx-auto md:h-screen',
          className
        )}
        ref={ref}
        {...props}
      />
    )
  }
)
FlexCentred.displayName = 'FlexCentred'

const FormContainer = React.forwardRef<HTMLFormElement, FormContainerProps>(
  ({ className, ...props }, ref) => {
    return (
      <form
        className={cn(
          'pt-4 space-y-4 w-full lg:space-y-8 lg:pt-8 lg:max-w-screen-sm',
          className
        )}
        ref={ref}
        {...props}
      />
    )
  }
)
FormContainer.displayName = 'FormContainer'

export { FlexCentred, FormContainer }
