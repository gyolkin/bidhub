from dataclasses import dataclass

from bidhub.infrastructure.env import getenv


@dataclass(frozen=True)
class DatabaseConfig:
    uri: str


def load_db_config() -> DatabaseConfig:
    db_uri = getenv('DB_URI')
    return DatabaseConfig(uri=db_uri)
