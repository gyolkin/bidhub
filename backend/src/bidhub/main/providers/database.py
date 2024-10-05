from dishka import Provider, Scope, provide, alias
from sqlalchemy.ext.asyncio import AsyncSession

from bidhub.infrastructure.sqla_db.gateways import SqlaUserGateway, SqlaBidGateway, SqlaAuctionGateway
from bidhub.infrastructure.sqla_db.tables import SqlaAuctionTable, SqlaBidTable
from bidhub.application.protocols.persistence import (
    IUnitOfWork,
    IUserGateway,
    IAuctionGateway,
    IBidGateway,
    IAuctionTable,
    IBidTable,
)


class DatabaseProvider(Provider):
    scope = Scope.REQUEST

    uow = alias(source=AsyncSession, provides=IUnitOfWork)

    user_gateway = provide(SqlaUserGateway, provides=IUserGateway)
    auction_gateway = provide(SqlaAuctionGateway, provides=IAuctionGateway)
    bid_gateway = provide(SqlaBidGateway, provides=IBidGateway)

    auction_table = provide(SqlaAuctionTable, provides=IAuctionTable)
    bid_table = provide(SqlaBidTable, provides=IBidTable)
