from bidhub.core.models import User
from bidhub.core.exceptions import AccessError


ACCESS_DENIED = 'Access denied.'


class AccessService:
    def allow_user_update(self, *, actor: User, resource: User) -> None:
        if actor.is_admin or actor.id == resource.id:
            return
        raise AccessError(ACCESS_DENIED)
