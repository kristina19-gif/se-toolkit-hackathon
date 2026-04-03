from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models import PlanResponse, Task, TaskCreate


app = FastAPI(title="AI Study Planner API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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


@app.get("/plan")
def generate_plan() -> PlanResponse:
    planned_tasks = sorted(
        [task for task in tasks if not task.done],
        key=lambda task: (-task.importance, task.effort, task.id),
    )
    explanation = (
        "Only tasks that are not done are shown. They are ordered by higher importance first "
        "and, when importance is the same, by lower effort first."
    )
    return PlanResponse(explanation=explanation, tasks=planned_tasks)


@app.patch("/tasks/{task_id}/done")
def update_task_done(task_id: int, done: bool) -> Task:
    for task in tasks:
        if task.id == task_id:
            task.done = done
            return task

    raise HTTPException(status_code=404, detail="Task not found")
