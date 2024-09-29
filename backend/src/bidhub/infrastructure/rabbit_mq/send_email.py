import json
from dataclasses import asdict

from aio_pika import Message as RabbitMessage, DeliveryMode
from aio_pika.abc import AbstractChannel as IRabbitChannel

from bidhub.application.protocols.task_queue import ISendEmailTask
from bidhub.application.dto.task_queue import SendWelcomeEmailInput


class RabbitSendEmailTask(ISendEmailTask):
    def __init__(self, rabbit_channel: IRabbitChannel) -> None:
        self.rabbit_channel = rabbit_channel

    async def __call__(
        self,
        *,
        message: SendWelcomeEmailInput,
    ) -> None:
        rabbit_message = RabbitMessage(
            body=json.dumps(asdict(message)).encode(),
            delivery_mode=DeliveryMode.PERSISTENT,
        )
        await self.rabbit_channel.default_exchange.publish(
            rabbit_message,
            routing_key='send_email',
        )
