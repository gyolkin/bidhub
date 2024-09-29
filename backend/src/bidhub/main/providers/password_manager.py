from dishka import Provider, Scope, provide

from bidhub.application.protocols.security import IPasswordManager
from bidhub.infrastructure.auth.password_manager import PasswordManager


class PasswordManagerProvider(Provider):
    scope = Scope.APP

    password_manager = provide(PasswordManager, provides=IPasswordManager)
