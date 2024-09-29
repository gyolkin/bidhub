import uuid

from sqlalchemy import (
    UUID,
    String,
    Integer,
    Column,
    Boolean,
    MetaData,
    Table,
    Boolean,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import registry, relationship

from bidhub.core.models import User, Auction, Bid


metadata_obj = MetaData()
mapper_registry = registry()

users = Table(
    'users',
    metadata_obj,
    Column('id', UUID, default=uuid.uuid4, primary_key=True),
    Column('email', String(255), unique=True, nullable=False),
    Column('password', String(255), nullable=False),
    Column('is_admin', Boolean, nullable=False),
    Column('created_at', DateTime, nullable=False),
)

auctions = Table(
    'auctions',
    metadata_obj,
    Column('id', UUID, default=uuid.uuid4, primary_key=True),
    Column('user_id', UUID, ForeignKey('users.id'), nullable=False),
    Column('title', String(255), nullable=False),
    Column('description', String(255), nullable=True),
    Column('start_price', Integer, nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('ending_at', DateTime, nullable=False),
)

bids = Table(
    'bids',
    metadata_obj,
    Column('id', UUID, default=uuid.uuid4, primary_key=True),
    Column('auction_id', UUID, ForeignKey('auctions.id'), nullable=False),
    Column('user_id', UUID, ForeignKey('users.id'), nullable=False),
    Column('amount', Integer, nullable=False),
    Column('created_at', DateTime, nullable=False),
)

mapper_registry.map_imperatively(User, users)
mapper_registry.map_imperatively(Auction, auctions, properties={'bids': relationship('Bid', back_populates='auction')})
mapper_registry.map_imperatively(
    Bid,
    bids,
    properties={
        'auction': relationship('Auction', back_populates='bids'),
        'user': relationship('User'),
    },
)
