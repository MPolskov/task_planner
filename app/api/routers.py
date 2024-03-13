from fastapi import APIRouter

from app.api.endpoints import (
    task_router
)

main_router = APIRouter()
main_router.include_router(
    task_router, prefix='/task', tags=['Task Planner']
)
