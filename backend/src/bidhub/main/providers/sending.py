from dishka import Provider, Scope, provide

from bidhub.application.protocols.sending import IEmailSender, INotificationService
from bidhub.infrastructure.sending.local_email import LocalEmailSender
from bidhub.infrastructure.sending.notification_service import NotificationService


class SendingProvider(Provider):
    scope = Scope.APP

    send_email = provide(LocalEmailSender, provides=IEmailSender)

    @provide
    def notification_service(
        self,
        email_sender: IEmailSender,
    ) -> INotificationService:
        return NotificationService(email_sender=email_sender)
