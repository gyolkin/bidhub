import { ArrowRight } from 'lucide-react'
import { Link } from 'react-router-dom'

import { AddAuctionDialog } from '@/features/auction/add'
import { Button, TypographyH1, TypographyH3 } from '@/shared/ui'

const WelcomeSection = () => {
  return (
    <section className="grid max-w-screen-xl px-4 py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12">
      <div className="mr-auto place-self-center lg:col-span-7">
        <TypographyH1 className="mb-4">
          Find Extraordinary Auctions Tailored to You
        </TypographyH1>
        <TypographyH3 className="mb-6 font-normal">
          Explore a world of unique auctions — whether you are searching for
          rare collectibles, luxury goods, or incredible deals, we have got
          something for everyone.
        </TypographyH3>
        <Button asChild className="mr-2 mb-2" size="lg">
          <Link to="/auctions">
            <span>Explore</span> <ArrowRight />
          </Link>
        </Button>
        <AddAuctionDialog type="button" />
      </div>
      <div className="hidden lg:mt-0 lg:col-span-5 lg:flex">
        <img src="/img/hammer.png" alt="hammer" />
      </div>
    </section>
  )
}

export { WelcomeSection }
