from abc import ABC, abstractmethod

from bidhub.application.dto.task_queue import ScheduleFinishAuctionRequest


class IScheduleFinishAuctionTask(ABC):
    @abstractmethod
    async def __call__(
        self,
        *,
        message: ScheduleFinishAuctionRequest,
    ) -> None:
        raise NotImplementedError
