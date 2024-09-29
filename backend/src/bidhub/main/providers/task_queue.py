from dishka import Provider, Scope, provide

from bidhub.application.protocols.task_queue import ISendEmailTask, IScheduleFinishAuctionTask
from bidhub.infrastructure.rabbit_mq.send_email import RabbitSendEmailTask
from bidhub.infrastructure.rabbit_mq.schedule_finish_auction import RabbitScheduleFinishAuctionTask


class TaskQueueProvider(Provider):
    scope = Scope.APP

    send_email_task = provide(RabbitSendEmailTask, provides=ISendEmailTask)
    finish_auction_task = provide(RabbitScheduleFinishAuctionTask, provides=IScheduleFinishAuctionTask)
