from bidhub.application.dto.task_queue import ScheduleFinishAuctionRequest
from bidhub.application.exceptions import NotFoundError
from bidhub.application.protocols.persistence import IAuctionGateway, IAuctionTable, IUnitOfWork
from bidhub.application.protocols.sending import INotificationService


class ScheduledAuctionFinish:
    def __init__(
        self,
        *,
        notification_service: INotificationService,
        auction_gateway: IAuctionGateway,
        auction_table: IAuctionTable,
        uow: IUnitOfWork,
    ):
        self.auction_gateway = auction_gateway
        self.auction_table = auction_table
        self.uow = uow
        self.notification_service = notification_service

    async def __call__(self, message: ScheduleFinishAuctionRequest) -> None:
        auction = await self.auction_gateway.get_auction_by_id(message.auction_id)
        detailed_auction = await self.auction_table.get_detailed_auction_by_id(message.auction_id)
        if auction is None or detailed_auction is None:
            raise NotFoundError()
        auction.close_auction()
        await self.auction_gateway.update_auction(auction)
        await self.uow.commit()

        if detailed_auction.highest_bid is None:
            await self.notification_service.notify_auction_finished_no_bids(
                owner_email=detailed_auction.user.email,
                auction_title=detailed_auction.title,
            )
        else:
            await self.notification_service.notify_auction_finished_with_winner(
                owner_email=detailed_auction.user.email,
                auction_title=detailed_auction.title,
                highest_bid_amount=detailed_auction.highest_bid.amount,
            )
            await self.notification_service.notify_auction_winner(
                winner_email=detailed_auction.highest_bid.user.email,
                auction_title=detailed_auction.title,
            )
