from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    importance: int = Field(ge=1, le=5)
    effort: int = Field(ge=1, le=5)


class Task(TaskCreate):
    id: int
    done: bool = False
