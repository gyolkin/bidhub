from fastapi import APIRouter

from .register import register
from .login import login
from .logout import logout


auth_router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)
auth_router.add_api_route(
    path='/register',
    summary='Register a new user',
    endpoint=register,
    methods=['POST'],
    status_code=201,
)
auth_router.add_api_route(
    path='/login',
    summary='Login a user',
    endpoint=login,
    methods=['POST'],
)
auth_router.add_api_route(
    path='/logout',
    summary='Logout a user',
    endpoint=logout,
    methods=['POST'],
    status_code=204,
)
