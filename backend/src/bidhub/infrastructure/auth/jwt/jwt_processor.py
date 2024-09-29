from datetime import datetime, timedelta
from uuid import UUID

import jwt

from bidhub.infrastructure.exceptions import InfrastructureError
from bidhub.core.models import UserId


JWT_ALGORITHM = 'HS256'


class JwtProcessor:
    def __init__(self, secret: str):
        self._secret = secret

    def encode(self, user_id: UserId, expires_in: int) -> str:
        issued_time = datetime.now()
        to_encode = {
            'sub': str(user_id),
            'iat': issued_time,
            'exp': issued_time + timedelta(seconds=expires_in),
        }
        return jwt.encode(to_encode, self._secret, algorithm=JWT_ALGORITHM)

    def decode(self, token: str) -> UserId:
        try:
            result = jwt.decode(token, self._secret, algorithms=[JWT_ALGORITHM])
            return UserId(UUID(result['sub']))
        except jwt.PyJWTError:
            raise InfrastructureError()
