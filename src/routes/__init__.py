from fastapi import APIRouter

from .api import api_router
from .ws import ws_router

main_router = APIRouter()

main_router.include_router(api_router, prefix="/api")
main_router.include_router(ws_router, prefix="/ws")
