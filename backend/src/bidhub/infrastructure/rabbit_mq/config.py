from dataclasses import dataclass

from bidhub.infrastructure.env import getenv


@dataclass(frozen=True)
class RabbitConfig:
    uri: str


def load_rabbit_config() -> RabbitConfig:
    rabbit_uri = getenv('RABBIT_URI')
    return RabbitConfig(uri=rabbit_uri)
