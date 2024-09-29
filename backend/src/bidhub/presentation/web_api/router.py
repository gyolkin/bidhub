from fastapi import APIRouter

from .auth.router import auth_router
from .user.router import user_router
from .auction.router import auction_router
from .bid.router import bid_router


router = APIRouter(prefix='/v1')
router.include_router(auth_router)
router.include_router(user_router)
router.include_router(auction_router)
router.include_router(bid_router)
