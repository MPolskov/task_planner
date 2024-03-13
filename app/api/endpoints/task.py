from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.task import task_crud
from app.schemas.task import (
    TaskCreate,
    TaskUpdate,
    TaskDB
)
from app.api.validators import check_task_exists

router = APIRouter()


@router.get(
    '/',
    response_model=list[TaskDB]
)
async def get_all_tasks(
    session: AsyncSession = Depends(get_async_session),
):
    """
    Получает список всех задач.
    """
    return await task_crud.get_multi(session)


@router.post(
    '/',
    response_model=TaskDB
)
async def create_task(
    task: TaskCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Создает новую задачу.
    """
    return await task_crud.create(task, session)


@router.delete(
    '/{task_id}',
    response_model=TaskDB
)
async def remove_task(
        task_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """
    Удаляет указанную задачу.
    """
    task = await check_task_exists(task_id, session)
    return await task_crud.remove(task, session)


@router.patch(
    '/{task_id}',
    response_model=TaskDB
)
async def partially_update_task(
        task_id: int,
        obj_in: TaskUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    """
    Изменяет указанную задачу.
    """
    task = await check_task_exists(
        task_id, session
    )
    return await task_crud.update(task, obj_in, session)
