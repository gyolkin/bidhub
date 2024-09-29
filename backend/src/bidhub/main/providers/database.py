from dishka import Provider, Scope, provide, alias
from sqlalchemy.ext.asyncio import AsyncSession

from bidhub.infrastructure.sqla_db.gateways import SqlaUserGateway, SqlaBidGateway, SqlaAuctionGateway
from bidhub.application.protocols.persistence import IUnitOfWork, IUserGateway, IAuctionGateway, IBidGateway


class DatabaseProvider(Provider):
    scope = Scope.REQUEST

    uow = alias(source=AsyncSession, provides=IUnitOfWork)
    user_gateway = provide(SqlaUserGateway, provides=IUserGateway)
    item_gateway = provide(SqlaAuctionGateway, provides=IAuctionGateway)
    bid_gateway = provide(SqlaBidGateway, provides=IBidGateway)
