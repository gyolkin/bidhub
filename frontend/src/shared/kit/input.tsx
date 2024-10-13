import React from 'react'

import { cn } from '../lib'
import { Input, type InputProps } from '../ui/input'

interface PriceInputProps extends Omit<InputProps, 'type'> {
  currencySymbol?: string
}

const PriceInput = React.forwardRef<HTMLInputElement, PriceInputProps>(
  ({ currencySymbol = '$', className, ...props }, ref) => {
    return (
      <div className="relative">
        <span className="absolute left-3 top-2 text-sm text-muted-foreground">
          {currencySymbol}
        </span>
        <Input
          type="number"
          className={cn('pl-8', className)}
          ref={ref}
          {...props}
        />
      </div>
    )
  }
)
PriceInput.displayName = 'PriceInput'

export { PriceInput }
