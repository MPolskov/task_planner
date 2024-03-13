from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.task import task_crud
from app.models import Task

NOT_FOUND = 'Задача не найдена!'


async def check_task_exists(
        task_id: int,
        session: AsyncSession,
) -> Task:
    task = await task_crud.get(task_id, session)
    if task is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=NOT_FOUND
        )
    return task
