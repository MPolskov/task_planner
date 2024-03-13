from typing import Optional
from enum import Enum

from pydantic import (
    BaseModel, Extra,
    Field, validator,
)


class Status(str, Enum):
    ADD = 'добавлена'
    IN_WORK = 'в работе'
    COMPLATED = 'выполнена'


MIN_LENGHT_NAME = 1
MAX_LENGHT_NAME = 100

NO_NAME = 'Имя задачи не может быть пустым!'
NO_DESCRIPTION = 'Описание задачи не может быть пустым!'


class TaskBase(BaseModel):
    name: Optional[str] = Field(
        None,
        min_length=MIN_LENGHT_NAME,
        max_length=MAX_LENGHT_NAME
    )
    description: Optional[str]
    status: Optional[Status]

    class Config:
        extra = Extra.forbid


class TaskUpdate(TaskBase):
    pass

    @validator('name')
    def name_cant_be_empty(cls, value: str):
        if value is None or value == '':
            raise ValueError(NO_NAME)
        return value

    @validator('description')
    def description_cant_be_empty(cls, value: str):
        if value is None or value == '':
            raise ValueError(NO_DESCRIPTION)
        return value


class TaskCreate(TaskUpdate):
    name: str = Field(
        ...,
        min_length=MIN_LENGHT_NAME,
        max_length=MAX_LENGHT_NAME
    )
    description: str
    status: Status


class TaskDB(TaskCreate):

    class Config:
        orm_mode = True
