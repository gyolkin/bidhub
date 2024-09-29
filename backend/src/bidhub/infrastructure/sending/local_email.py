import sys

from bidhub.application.protocols.sending import IEmailSender


class LocalEmailSender(IEmailSender):
    async def __call__(
        self,
        *,
        email: str,
        subject: str,
        message: str,
    ) -> None:
        sys.stdout.write(
            'Email has been successfully sent.\n\n' f'TO: {email}\n' f'SUBJECT: {subject}\n' f'MESSAGE: {message}\n'
        )
