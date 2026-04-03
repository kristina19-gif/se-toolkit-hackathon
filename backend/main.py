from fastapi import FastAPI

from models import Task, TaskCreate


app = FastAPI(title="AI Study Planner API")
tasks: list[Task] = []


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "AI Study Planner backend is running."
    }


@app.get("/tasks")
def list_tasks() -> list[Task]:
    return tasks


@app.post("/tasks")
def create_task(task: TaskCreate) -> Task:
    created_task = Task(
        id=len(tasks) + 1,
        title=task.title,
        importance=task.importance,
        effort=task.effort,
        done=False,
    )
    tasks.append(created_task)
    return created_task
