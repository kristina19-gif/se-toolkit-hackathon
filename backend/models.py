from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class TaskBase(SQLModel):
    title: str = Field(min_length=1, max_length=200)
    importance: int = Field(ge=1, le=5)
    effort: int = Field(ge=1, le=5)
    done: bool = False


class TaskCreate(TaskBase):
    pass


class Task(TaskBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class PlanResponse(BaseModel):
    explanation: str
    tasks: list[Task]
