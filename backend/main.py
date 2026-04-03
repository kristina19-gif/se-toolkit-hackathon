from fastapi import FastAPI


app = FastAPI(title="AI Study Planner API")


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "AI Study Planner backend is running."
    }
