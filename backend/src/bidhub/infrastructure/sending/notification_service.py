from bidhub.application.protocols.sending import INotificationService, IEmailSender


class NotificationService(INotificationService):
    def __init__(self, email_sender: IEmailSender):
        self.email_sender = email_sender

    async def notify_auction_finished_no_bids(
        self,
        owner_email: str,
        auction_title: str,
    ) -> None:
        await self.email_sender(
            email=owner_email,
            subject='Your Auction Has Ended',
            message=(
                f'Dear {owner_email},\n\n'
                f'Unfortunately, your auction for {auction_title} has ended without any bids.\n\n'
                'Best regards,\n'
                'The BidHub Team'
            ),
        )

    async def notify_auction_finished_with_winner(
        self,
        owner_email: str,
        auction_title: str,
        highest_bid_amount: int,
    ) -> None:
        await self.email_sender(
            email=owner_email,
            subject='Congratulations, Your Auction Has Successfully Ended!',
            message=(
                f'Dear {owner_email},\n\n'
                f'Congratulations! Your auction for {auction_title} has successfully ended '
                f'with a final price of ${highest_bid_amount}.\n\n'
                'Best regards,\n'
                'The BidHub Team'
            ),
        )

    async def notify_auction_winner(self, winner_email: str, auction_title: str) -> None:
        await self.email_sender(
            email=winner_email,
            subject=f'Congratulations on Winning the {auction_title} Auction!',
            message=(
                f'Dear {winner_email},\n\n'
                f'Congratulations! You are the proud winner of the {auction_title}. Thank you '
                'for participating, and we hope you enjoy your new purchase!\n\n'
                'Best regards,\n'
                'The BidHub Team'
            ),
        )
