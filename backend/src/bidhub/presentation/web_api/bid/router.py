from fastapi import APIRouter

from .create import create_bid
from .list import list_bids


bid_router = APIRouter(
    prefix='/bids',
    tags=['bids'],
)
bid_router.add_api_route(
    path='/',
    summary='Place Bid',
    endpoint=create_bid,
    methods=['POST'],
)
bid_router.add_api_route(
    path='/',
    summary='List Bids',
    endpoint=list_bids,
    methods=['GET'],
)
