import { cva, type VariantProps } from 'class-variance-authority'
import { AlertCircle } from 'lucide-react'
import React from 'react'

import { cn } from '../lib'

const alertVariants = cva(
  'relative w-full rounded-lg border p-4 [&>svg~*]:pl-7 [&>svg+div]:translate-y-[-3px] [&>svg]:absolute [&>svg]:left-4 [&>svg]:top-4',
  {
    variants: {
      variant: {
        default: 'bg-background text-foreground',
        destructive:
          'border-destructive/50 text-destructive dark:border-destructive [&>svg]:text-destructive',
      },
    },
    defaultVariants: {
      variant: 'default',
    },
  }
)

const Alert = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement> & VariantProps<typeof alertVariants>
>(({ className, variant, ...props }, ref) => (
  <div
    ref={ref}
    role="alert"
    className={cn(alertVariants({ variant }), className)}
    {...props}
  />
))
Alert.displayName = 'Alert'

const AlertTitle = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLHeadingElement>
>(({ className, ...props }, ref) => (
  <h5
    ref={ref}
    className={cn('mb-1 font-medium leading-none tracking-tight', className)}
    {...props}
  />
))
AlertTitle.displayName = 'AlertTitle'

const AlertDescription = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLParagraphElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn('text-sm [&_p]:leading-relaxed', className)}
    {...props}
  />
))
AlertDescription.displayName = 'AlertDescription'

interface AlertDestructiveProps extends React.HTMLAttributes<HTMLDivElement> {
  title?: string
}

const AlertDestructive = React.forwardRef<
  HTMLDivElement,
  AlertDestructiveProps
>(({ title, children, ...props }, ref) => (
  <Alert variant="destructive" ref={ref} {...props}>
    {title && (
      <>
        <AlertCircle className="h-4 w-4" />
        <AlertTitle>{title}</AlertTitle>
      </>
    )}
    <AlertDescription>{children}</AlertDescription>
  </Alert>
))
AlertDestructive.displayName = 'AlertDestructive'

export { Alert, AlertDescription, AlertDestructive, AlertTitle }
