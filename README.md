# AI Study Planner

A web app that helps students turn a list of study tasks into a prioritized daily plan.

## Demo

Deployed product: [http://10.93.24.148:8080/](http://10.93.24.148:8080/)

### Main Page

![Main page](./%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-04-05%20101058.png)

### Task List And Study Plan

![Task list and study plan](./%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-04-05%20101350.png)

## Product Context

### End Users

University students who need help deciding what to study first.

### Problem

Students often have several study tasks at the same time and do not know how to prioritize them.

### Solution

AI Study Planner lets the user enter tasks with importance and effort, view all current tasks, generate a prioritized study plan, and mark tasks as done or not done.

## Features

### Implemented

- add study tasks
- view all tasks
- generate a prioritized study plan
- show a short explanation of the planning logic
- mark tasks as done or not done
- exclude completed tasks from the generated plan
- deploy the app on a VM with Docker Compose

### Not Yet Implemented

- polished UI styling

## Usage

1. Start the backend:

   ```powershell
   cd C:\Users\krist\se-toolkit-hackathon\backend
   uv sync
   uv run uvicorn main:app --reload
   ```

2. Open the app in the browser:

   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

3. Add a task by entering:

   - title
   - importance from 1 to 5
   - effort from 1 to 5

4. Submit the form to add the task.

5. The task list and the prioritized study plan update automatically.

6. Use the status button in the task list to mark a task as done or not done.

7. Completed tasks stay in the task list but disappear from the generated plan.

## Deployment

### Target OS

Ubuntu 24.04

### What Should Be Installed

- `git`
- `Python 3.11+`
- `uv`
- a web browser
- `Docker`
- `Docker Compose`

### Step-by-Step Deployment

1. Clone the repository:

   ```bash
   git clone --branch kristi https://github.com/kristina19-gif/se-toolkit-hackathon.git
   cd se-toolkit-hackathon
   ```

2. Start the app:

   ```bash
   docker compose up --build -d
   ```

3. Open the deployed app in the browser:

   ```text
   http://<vm-ip>:8080/
   ```

4. To stop the app:

   ```bash
   docker compose down
   ```
