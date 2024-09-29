from typing import Callable, TypeVar

from bidhub.application.protocols.security import IUserIdentity


T = TypeVar('T')
WithAuth = Callable[[IUserIdentity], T]
