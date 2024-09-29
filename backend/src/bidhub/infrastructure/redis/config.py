from dataclasses import dataclass

from bidhub.infrastructure.env import getenv


@dataclass(frozen=True)
class RedisConfig:
    uri: str


def load_redis_config() -> RedisConfig:
    redis_uri = getenv('REDIS_URI')
    return RedisConfig(uri=redis_uri)
