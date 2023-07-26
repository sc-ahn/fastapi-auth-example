from fastapi import APIRouter

from user.routes import router as user_router

routers = APIRouter(prefix="/api")

routers.include_router(user_router)
