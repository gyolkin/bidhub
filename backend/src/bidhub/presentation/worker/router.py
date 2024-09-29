from faststream.rabbit import RabbitRoute, RabbitRouter, RabbitExchange, ExchangeType

from .send_email import send_welcome_email
from .schedule_finish_auction import schedule_finish_auction


delayed_exchange = RabbitExchange(
    name='delayed_exchange',
    type=ExchangeType.X_DELAYED_MESSAGE,
    arguments={'x-delayed-type': ExchangeType.DIRECT},
)

router = RabbitRouter(
    handlers=[
        RabbitRoute(
            send_welcome_email,
            queue='send_email',
        ),
        RabbitRoute(
            schedule_finish_auction,
            queue='close_auction',
            exchange=delayed_exchange,
        ),
    ],
)
