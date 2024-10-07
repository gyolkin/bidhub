import { AuctionList } from '@/widgets/auction-list'
import { WelcomeSection } from '@/widgets/welcome-section'
import { AuctionSearchForm } from '@/features/auction/search'
import { TypographyH3 } from '@/shared/ui'

const HomePage = () => {
  return (
    <div className="py-10 space-y-4">
      <WelcomeSection />
      <TypographyH3 className="text-center">
        There are <strong>1,000+</strong> auctions for you
      </TypographyH3>
      <AuctionSearchForm />
      <AuctionList />
    </div>
  )
}

export { HomePage }
