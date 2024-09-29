from dishka import Provider, Scope, provide

from bidhub.core.validators import EmailValidator, PasswordValidator


class ValidatorsProvider(Provider):
    scope = Scope.APP

    validate_email = provide(EmailValidator, provides=EmailValidator)
    validate_password = provide(PasswordValidator, provides=PasswordValidator)
