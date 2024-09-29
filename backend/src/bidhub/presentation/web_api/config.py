from dataclasses import dataclass

from bidhub.infrastructure.env import getenv


@dataclass(frozen=True)
class WebConfig:
    base_url: str
    jwt_secret: str


def load_web_config() -> WebConfig:
    base_url = getenv('BASE_URL')
    jwt_secret = getenv('JWT_SECRET')
    return WebConfig(
        base_url=base_url,
        jwt_secret=jwt_secret,
    )
