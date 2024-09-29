import json
from dataclasses import asdict

from aio_pika import Message as RabbitMessage, DeliveryMode
from aio_pika.abc import AbstractChannel as IRabbitChannel

from bidhub.infrastructure.json_encoder import UUIDEncoder
from bidhub.application.protocols.task_queue import IScheduleFinishAuctionTask
from bidhub.application.dto.task_queue import ScheduleFinishAuctionInput


MINUTE_IN_MILLISECONDS = 60 * 1000


class RabbitScheduleFinishAuctionTask(IScheduleFinishAuctionTask):
    def __init__(self, rabbit_channel: IRabbitChannel) -> None:
        self.rabbit_channel = rabbit_channel

    async def __call__(
        self,
        *,
        message: ScheduleFinishAuctionInput,
    ) -> None:
        exchange = await self.rabbit_channel.get_exchange('delayed_exchange')
        rabbit_message = RabbitMessage(
            body=json.dumps(asdict(message), cls=UUIDEncoder).encode(),
            headers={'x-delay': message.mins_to_finish * MINUTE_IN_MILLISECONDS},
            delivery_mode=DeliveryMode.PERSISTENT,
        )
        await exchange.publish(
            rabbit_message,
            routing_key='close_auction',
        )
