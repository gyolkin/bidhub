from dishka.integrations.faststream import FromDishka, inject

from bidhub.application.dto.task_queue import ScheduleFinishAuctionInput
from bidhub.application.usecases.task_queue import FinishAuction


@inject
async def schedule_finish_auction(
    usecase: FromDishka[FinishAuction],
    message: ScheduleFinishAuctionInput,
) -> None:
    await usecase(message)
