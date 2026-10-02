from datetime import date

from sqlalchemy import Boolean, Date, String
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    course: Mapped[str] = mapped_column(String(100))
    due_date: Mapped[date] = mapped_column(Date)
    priority: Mapped[int] = mapped_column(default=2)  # 1 = high, 3 = low
    done: Mapped[bool] = mapped_column(Boolean, default=False)
