from bidhub.application.dto.task_queue import ScheduleFinishAuctionInput
from bidhub.application.protocols.persistence import IAuctionGateway, IBidGateway, IUserGateway, IUnitOfWork
from bidhub.application.protocols.sending import INotificationService


class FinishAuction:
    def __init__(
        self,
        *,
        notification_service: INotificationService,
        auction_gateway: IAuctionGateway,
        bid_gateway: IBidGateway,
        user_gateway: IUserGateway,
        uow: IUnitOfWork,
    ):
        self.auction_gateway = auction_gateway
        self.bid_gateway = bid_gateway
        self.user_gateway = user_gateway
        self.uow = uow
        self.notification_service = notification_service

    async def __call__(self, message: ScheduleFinishAuctionInput) -> None:
        current_auction = await self.auction_gateway.get_auction_by_id(message.auction_id)
        if current_auction is None:
            return
        current_auction.close_auction()
        await self.auction_gateway.update_auction(current_auction)

        auction_owner = await self.user_gateway.get_user_by_id(current_auction.user_id)
        if auction_owner is None:
            return
        highest_bid = await self.bid_gateway.get_highest_bid_by_auction(current_auction.id)
        if highest_bid is None:
            await self.notification_service.notify_auction_finished_no_bids(
                owner=auction_owner, auction=current_auction
            )
        else:
            winner = await self.user_gateway.get_user_by_id(highest_bid.user_id)
            if winner is not None:
                await self.notification_service.notify_auction_finished_with_winner(
                    owner=auction_owner,
                    auction=current_auction,
                    highest_bid=highest_bid,
                )
                await self.notification_service.notify_auction_winner(
                    winner=winner,
                    auction=current_auction,
                )
        await self.uow.commit()
