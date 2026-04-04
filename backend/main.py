from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlmodel import Session, select

from database import create_db_and_tables, get_session
from models import PlanResponse, Task, TaskCreate


app = FastAPI(title="AI Study Planner API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
frontend_dir = Path(__file__).resolve().parent.parent / "frontend"


@app.on_event("startup")
def on_startup() -> None:
    create_db_and_tables()


@app.get("/")
def read_root() -> FileResponse:
    return FileResponse(frontend_dir / "index.html")


@app.get("/app.js")
def read_app_js() -> FileResponse:
    return FileResponse(frontend_dir / "app.js", media_type="text/javascript")


@app.get("/tasks")
def list_tasks() -> list[Task]:
    with get_session() as session:
        return list(session.exec(select(Task)))


@app.post("/tasks")
def create_task(task: TaskCreate) -> Task:
    created_task = Task.model_validate(task)
    with get_session() as session:
        session.add(created_task)
        session.commit()
        session.refresh(created_task)
        return created_task


@app.get("/plan")
def generate_plan() -> PlanResponse:
    with get_session() as session:
        tasks = list(session.exec(select(Task)))

    planned_tasks = sorted(
        [task for task in tasks if not task.done],
        key=lambda task: (-task.importance, task.effort, task.id or 0),
    )
    explanation = (
        "Only tasks that are not done are shown. They are ordered by higher importance first "
        "and, when importance is the same, by lower effort first."
    )
    return PlanResponse(explanation=explanation, tasks=planned_tasks)


@app.patch("/tasks/{task_id}/done")
def update_task_done(task_id: int, done: bool) -> Task:
    with get_session() as session:
        task = session.get(Task, task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")

        task.done = done
        session.add(task)
        session.commit()
        session.refresh(task)
        return task
