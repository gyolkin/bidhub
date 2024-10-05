from dishka.integrations.faststream import FromDishka, inject

from bidhub.application.dto.task_queue import ScheduleFinishAuctionRequest
from bidhub.application.usecases.task_queue import ScheduledAuctionFinish


@inject
async def schedule_finish_auction(
    usecase: FromDishka[ScheduledAuctionFinish],
    message: ScheduleFinishAuctionRequest,
) -> None:
    await usecase(message)
