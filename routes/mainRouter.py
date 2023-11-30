from fastapi import APIRouter
from routes.searchRouter import searchRouter

mainRouter = APIRouter()

mainRouter.include_router(searchRouter)
