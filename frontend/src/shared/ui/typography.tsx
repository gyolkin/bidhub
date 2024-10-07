import React from 'react'

import { cn } from '@/shared/lib'

export interface TypographyPProps
  extends React.HTMLAttributes<HTMLParagraphElement> {
  muted?: boolean
}

export interface TypographyHProps
  extends React.HTMLAttributes<HTMLHeadingElement> {}

const TypographyP = ({ className, muted, ...props }: TypographyPProps) => {
  return (
    <p
      className={cn('leading-4', muted && 'text-muted-foreground', className)}
      {...props}
    />
  )
}

const TypographyH1 = ({ className, ...props }: TypographyHProps) => {
  return (
    <h1
      className={cn(
        'scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl',
        className
      )}
      {...props}
    />
  )
}

const TypographyH2 = ({ className, ...props }: TypographyHProps) => {
  return (
    <h1
      className={cn(
        'scroll-m-20 pb-2 text-3xl font-semibold tracking-tight first:mt-0',
        className
      )}
      {...props}
    />
  )
}

const TypographyH3 = ({ className, ...props }: TypographyHProps) => {
  return (
    <h1
      className={cn(
        'scroll-m-20 text-2xl font-semibold tracking-tight',
        className
      )}
      {...props}
    />
  )
}

export { TypographyH1, TypographyH2, TypographyH3, TypographyP }
