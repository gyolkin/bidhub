from bidhub.core.exceptions import ValidationError

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 32
TOO_SHORT_PASSWORD = 'Password must be at least 8 characters long.'
TOO_LONG_PASSWORD = 'Password must be at most 32 characters long.'
PASSWORD_NEED_DIGITS = 'Password must contain at least one digit.'
PASSWORD_NEED_UPPERCASE = 'Password must contain at least one uppercase letter.'


class PasswordValidator:
    def __call__(self, password: str) -> None:
        if len(password) < MIN_PASSWORD_LENGTH:
            raise ValidationError(TOO_SHORT_PASSWORD)
        if len(password) > MAX_PASSWORD_LENGTH:
            raise ValidationError(TOO_LONG_PASSWORD)
        if not any(char.isdigit() for char in password):
            raise ValidationError(PASSWORD_NEED_DIGITS)
        if not any(char.isupper() for char in password):
            raise ValidationError(PASSWORD_NEED_UPPERCASE)
