import uuid
from datetime import datetime

from sqlalchemy import UUID, DateTime, Integer, Text, func
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import Mapped, mapped_column

from constants.task import TaskStatus
from databases.database import Base


class Task(Base):
    """
    Модель задачи

    ## Attrs:
        - id: int - идентификатор
        - uid: UUID -  идентификатор
        - created_at: datetime - дата и время
            создания ззадачи
        - status: TaskStatus - статус задачи
    """

    __tablename__ = "task"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    uid: Mapped[uuid.UUID] = mapped_column(
        UUID, unique=True, index=True, default=uuid.uuid4
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    description: Mapped[str] = mapped_column(Text, default="")
    status: Mapped[ENUM] = mapped_column(
        ENUM(TaskStatus, create_type=False),
    )
