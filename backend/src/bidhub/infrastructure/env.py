import os

from bidhub.infrastructure.exceptions import InfrastructureError


class ConfigParseError(InfrastructureError):
    pass


def getenv(key) -> str:
    value = os.getenv(key)
    if value is None:
        raise ConfigParseError(f'{key} environmental variable is not set')
    return value
