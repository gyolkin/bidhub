from bidhub.application.dto.auction import CreateAuctionInput, AuctionIdOutput
from bidhub.application.dto.task_queue import ScheduleFinishAuctionInput
from bidhub.application.protocols.persistence import IUnitOfWork, IAuctionGateway
from bidhub.application.protocols.security import IUserIdentity
from bidhub.application.protocols.task_queue import IScheduleFinishAuctionTask
from bidhub.core.services import AuctionService
from bidhub.core.models import AuctionId


class StartAuction:
    def __init__(
        self,
        *,
        user_identity: IUserIdentity,
        auction_service: AuctionService,
        auction_gateway: IAuctionGateway,
        uow: IUnitOfWork,
        finish_auction_task: IScheduleFinishAuctionTask,
    ):
        self.user_identity = user_identity
        self.auction_service = auction_service
        self.auction_gateway = auction_gateway
        self.uow = uow
        self.finish_auction_task = finish_auction_task

    async def __call__(self, request: CreateAuctionInput) -> AuctionIdOutput:
        current_user = await self.user_identity.get_current_user()
        new_auction = self.auction_service.create_auction(
            user_id=current_user.id,
            title=request.title,
            description=request.description,
            start_price=request.start_price,
            days_to_finish=request.days_to_finish,
        )
        await self.auction_gateway.save_auction(new_auction)
        await self.uow.commit()
        await self._schedule_finish_auction_task(new_auction.id, request.days_to_finish)
        return AuctionIdOutput(new_auction.id)

    async def _schedule_finish_auction_task(self, auction_id: AuctionId, days_to_finish: int):
        message = ScheduleFinishAuctionInput(
            auction_id=auction_id,
            days_to_finish=days_to_finish,
        )
        await self.finish_auction_task(message=message)
