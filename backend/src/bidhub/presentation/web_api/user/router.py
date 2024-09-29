from fastapi import APIRouter

from .retrieve import get_user
from .update import update_user
from .current import get_current_user


user_router = APIRouter(
    prefix='/users',
    tags=['users'],
)
user_router.add_api_route(
    path='/me',
    summary='Get current user',
    endpoint=get_current_user,
    methods=['GET'],
)
user_router.add_api_route(
    path='/{user_id}',
    summary='Get user by id',
    endpoint=get_user,
    methods=['GET'],
)
user_router.add_api_route(
    path='/{user_id}',
    summary='Update user',
    endpoint=update_user,
    methods=['PATCH'],
)
