from fastapi import APIRouter

from .create import create_auction
from .list import list_auctions
from .retrieve import get_auction


auction_router = APIRouter(
    prefix='/auctions',
    tags=['auctions'],
)
auction_router.add_api_route(
    path='/',
    summary='Create',
    endpoint=create_auction,
    methods=['POST'],
)
auction_router.add_api_route(
    path='/',
    summary='List Auctions',
    endpoint=list_auctions,
    methods=['GET'],
)
auction_router.add_api_route(
    path='/{auction_id}',
    summary='Get Auction',
    endpoint=get_auction,
    methods=['GET'],
)
