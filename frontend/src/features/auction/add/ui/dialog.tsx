import { Plus } from 'lucide-react'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

import { usersApi } from '@/entities/user'
import {
  Button,
  Card,
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '@/shared/ui'

import { AddAuctionForm } from './form'

interface AddButtonDialogProps {
  type: 'card' | 'button'
}

const AddAuctionDialog = ({ type }: AddButtonDialogProps) => {
  const navigate = useNavigate()
  const { data: user } = usersApi.endpoints.getCurrentUser.useQueryState()
  const [isOpen, setIsOpen] = useState(false)
  const handleDialogOpen = () => {
    if (!user) {
      navigate('/login')
    } else {
      setIsOpen(!isOpen)
    }
  }
  return (
    <Dialog open={isOpen} onOpenChange={handleDialogOpen}>
      <DialogTrigger asChild>
        {type === 'card' ? (
          <Card className="flex flex-col justify-center items-center p-6 mx-auto h-full w-full cursor-pointer hover:border-dashed">
            <Plus /> <span>Add Item</span>
          </Card>
        ) : (
          <Button variant="outline" size="lg">
            <span>Add Item</span> <Plus />
          </Button>
        )}
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Add New Auction</DialogTitle>
          <DialogDescription>
            We are happy you decided to add a new auction!
          </DialogDescription>
        </DialogHeader>
        <AddAuctionForm />
      </DialogContent>
    </Dialog>
  )
}

export { AddAuctionDialog }
