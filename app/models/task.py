from sqlalchemy import Column, String, Text

from app.core.db import Base


class Task(Base):
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(String(10), nullable=False)
