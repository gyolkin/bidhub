from dishka import Provider, Scope, provide

from bidhub.core.validators import EmailValidator, PasswordValidator
from bidhub.core.services import UserService, AuctionService, BidService, AccessService


class ServicesProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def user_service(
        self,
        password_validator: PasswordValidator,
        email_validator: EmailValidator,
    ) -> UserService:
        return UserService(
            password_validator=password_validator,
            email_validator=email_validator,
        )

    auction_service = provide(AuctionService, provides=AuctionService)
    bid_service = provide(BidService, provides=BidService)
    access_service = provide(AccessService, provides=AccessService)
