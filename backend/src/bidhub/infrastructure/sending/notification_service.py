from bidhub.application.protocols.sending import INotificationService, IEmailSender
from bidhub.core.models import User, Auction, Bid


class NotificationService(INotificationService):
    def __init__(self, email_sender: IEmailSender):
        self.email_sender = email_sender

    async def notify_auction_finished_no_bids(self, owner: User, auction: Auction) -> None:
        await self.email_sender(
            email=owner.email,
            subject='Your Auction Has Ended',
            message=(
                f'Dear {owner.email},\n\n'
                f'Unfortunately, your auction for {auction.title} has ended without any bids.\n\n'
                'Best regards,\n'
                'The BidHub Team'
            ),
        )

    async def notify_auction_finished_with_winner(self, owner: User, auction: Auction, highest_bid: Bid) -> None:
        await self.email_sender(
            email=owner.email,
            subject='Congratulations, Your Auction Has Successfully Ended!',
            message=(
                f'Dear {owner.email},\n\n'
                f'Congratulations! Your auction for {auction.title} has successfully ended '
                f'with a final price of ${highest_bid.amount}.\n\n'
                'Best regards,\n'
                'The BidHub Team'
            ),
        )

    async def notify_auction_winner(self, winner: User, auction: Auction) -> None:
        await self.email_sender(
            email=winner.email,
            subject=f'Congratulations on Winning the {auction.title} Auction!',
            message=(
                f'Dear {winner.email},\n\n'
                f'Congratulations! You are the proud winner of the {auction.title}. Thank you '
                'for participating, and we hope you enjoy your new purchase!\n\n'
                'Best regards,\n'
                'The BidHub Team'
            ),
        )
