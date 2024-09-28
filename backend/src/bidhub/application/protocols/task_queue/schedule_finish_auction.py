from abc import ABC, abstractmethod

from bidhub.application.dto.task_queue import ScheduleFinishAuctionInput


class IScheduleFinishAuctionTask(ABC):
    @abstractmethod
    async def __call__(
        self,
        *,
        message: ScheduleFinishAuctionInput,
    ) -> None:
        raise NotImplementedError
