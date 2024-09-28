from bidhub.application.dto.task_queue import SendWelcomeEmailInput
from bidhub.application.protocols.sending import IEmailSender


class SendWelcomeEmail:
    def __init__(
        self,
        *,
        email_sender: IEmailSender,
    ):
        self.send_email = email_sender

    async def __call__(self, message: SendWelcomeEmailInput) -> None:
        await self.send_email(
            email=message.receiver,
            subject='Welcome to BidHub!',
             message=(
                f'Dear {message.receiver},\n\n'
                'Welcome to BidHub! We are excited to have you with us and look forward to '
                'helping you explore everything we have to offer.\n\n'
                'Best regards,\n'
                'The BidHub Team'
            ),
        )
