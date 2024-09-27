import re

from bidhub.core.exceptions import ValidationError


INVALID_EMAIL = 'Please enter a valid email address.'


class EmailValidator:
    def __call__(self, email: str) -> None:
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not re.match(regex, email):
            raise ValidationError(INVALID_EMAIL)
