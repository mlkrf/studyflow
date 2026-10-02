from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    course: str = Field(min_length=1, max_length=100)
    due_date: date
    priority: int = Field(default=2, ge=1, le=3)


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    course: Optional[str] = None
    due_date: Optional[date] = None
    priority: Optional[int] = Field(default=None, ge=1, le=3)
    done: Optional[bool] = None


class TaskOut(TaskCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    done: bool
