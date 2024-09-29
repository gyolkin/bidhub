from dishka import Provider, Scope, provide

from bidhub.presentation.auth_guard import WithAuth
from bidhub.application.usecases.user import (
    RegisterUser,
    GetUser,
    GetCurrentUser,
    UpdateUser,
    AuthenticateUser,
)
from bidhub.application.usecases.task_queue import (
    SendWelcomeEmail,
    FinishAuction,
)
from bidhub.application.usecases.bid import (
    PlaceBid,
    ListBids,
)
from bidhub.application.usecases.auction import (
    StartAuction,
    GetAuction,
    ListAuctions,
)

from bidhub.application.protocols.task_queue import (
    ISendEmailTask,
    IScheduleFinishAuctionTask,
)
from bidhub.application.protocols.sending import IEmailSender, INotificationService
from bidhub.application.protocols.persistence import IUnitOfWork, IAuctionGateway, IBidGateway, IUserGateway
from bidhub.application.protocols.security import IUserIdentity, IPasswordManager
from bidhub.core.services import UserService, AuctionService, BidService, AccessService


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def register_user(
        self,
        user_service: UserService,
        user_gateway: IUserGateway,
        uow: IUnitOfWork,
        send_email_task: ISendEmailTask,
        password_manager: IPasswordManager,
    ) -> RegisterUser:
        return RegisterUser(
            user_service=user_service,
            user_gateway=user_gateway,
            uow=uow,
            send_email_task=send_email_task,
            password_manager=password_manager,
        )

    @provide
    def get_user(
        self,
        user_gateway: IUserGateway,
    ) -> GetUser:
        return GetUser(user_gateway=user_gateway)

    @provide
    def get_current_user(self) -> WithAuth[GetCurrentUser]:
        def require(user_identity: IUserIdentity):
            return GetCurrentUser(user_identity=user_identity)

        return require

    @provide
    def update_user(
        self,
        access_service: AccessService,
        user_service: UserService,
        user_gateway: IUserGateway,
        uow: IUnitOfWork,
        password_manager: IPasswordManager,
    ) -> WithAuth[UpdateUser]:
        def require(user_identity: IUserIdentity):
            return UpdateUser(
                access_service=access_service,
                user_identity=user_identity,
                user_service=user_service,
                user_gateway=user_gateway,
                uow=uow,
                password_manager=password_manager,
            )

        return require

    @provide
    def authenticate_user(
        self,
        user_gateway: IUserGateway,
        password_manager: IPasswordManager,
    ) -> AuthenticateUser:
        return AuthenticateUser(
            user_gateway=user_gateway,
            password_manager=password_manager,
        )

    @provide
    def start_auction(
        self,
        uow: IUnitOfWork,
        auction_service: AuctionService,
        auction_gateway: IAuctionGateway,
        finish_auction_task: IScheduleFinishAuctionTask,
    ) -> WithAuth[StartAuction]:
        def require(user_identity: IUserIdentity):
            return StartAuction(
                user_identity=user_identity,
                auction_service=auction_service,
                auction_gateway=auction_gateway,
                uow=uow,
                finish_auction_task=finish_auction_task,
            )

        return require

    @provide
    def get_auction(
        self,
        user_gateway: IUserGateway,
        auction_gateway: IAuctionGateway,
    ) -> GetAuction:
        return GetAuction(
            user_gateway=user_gateway,
            auction_gateway=auction_gateway,
        )

    @provide
    def list_auctions(
        self,
        user_gateway: IUserGateway,
        auction_gateway: IAuctionGateway,
    ) -> ListAuctions:
        return ListAuctions(
            user_gateway=user_gateway,
            auction_gateway=auction_gateway,
        )

    @provide
    def place_bid(
        self,
        uow: IUnitOfWork,
        bid_service: BidService,
        bid_gateway: IBidGateway,
        auction_gateway: IAuctionGateway,
    ) -> WithAuth[PlaceBid]:
        def require(user_identity: IUserIdentity):
            return PlaceBid(
                user_identity=user_identity,
                bid_service=bid_service,
                bid_gateway=bid_gateway,
                auction_gateway=auction_gateway,
                uow=uow,
            )

        return require

    @provide
    def list_bids(
        self,
        user_gateway: IUserGateway,
        auction_gateway: IAuctionGateway,
        bid_gateway: IBidGateway,
    ) -> ListBids:
        return ListBids(
            user_gateway=user_gateway,
            auction_gateway=auction_gateway,
            bid_gateway=bid_gateway,
        )

    @provide
    def send_welcome_email(
        self,
        email_sender: IEmailSender,
    ) -> SendWelcomeEmail:
        return SendWelcomeEmail(email_sender=email_sender)

    @provide
    def finish_auction(
        self,
        auction_gateway: IAuctionGateway,
        bid_gateway: IBidGateway,
        user_gateway: IUserGateway,
        uow: IUnitOfWork,
        notification_service: INotificationService,
    ) -> FinishAuction:
        return FinishAuction(
            auction_gateway=auction_gateway,
            bid_gateway=bid_gateway,
            user_gateway=user_gateway,
            uow=uow,
            notification_service=notification_service,
        )
