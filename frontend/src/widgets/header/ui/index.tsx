interface HeaderProps {
  navigationSlot?: React.ReactNode
  themeSwitcherSlot?: React.ReactNode
  userSlot?: React.ReactNode
}

const Header = ({
  navigationSlot,
  themeSwitcherSlot,
  userSlot,
}: HeaderProps) => {
  return (
    <header className="sticky top-0 mx-auto flex flex-row justify-between items-center p-4 lg:max-w-screen-2xl bg-background">
      <h2>BidHub</h2>
      <div className="flex items-center gap-3">
        {navigationSlot}
        {themeSwitcherSlot}
        {userSlot}
      </div>
    </header>
  )
}

export { Header }
