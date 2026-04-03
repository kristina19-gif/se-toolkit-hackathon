# AI Study Planner

AI Study Planner is a web app that turns a student's task list into a clear prioritized study plan for the day.

## Product Context

- End-user: university students
- Problem: students often have many tasks and deadlines but do not know what to do first
- Core feature: the user enters tasks, and the app generates a prioritized daily plan with a short AI explanation of the order

## Architecture

This project will have three parts:

- `frontend` - a React web app running in the browser
- `backend` - a FastAPI service with the business logic and API
- `database` - a PostgreSQL database storing tasks

This is called separation of concerns:

- the frontend is responsible for input and output
- the backend is responsible for logic and HTTP endpoints
- the database is responsible for persistence

## Product Versions

### Version 1

- add tasks
- view all tasks
- generate a prioritized study plan

### Version 2

- add tasks
- view all tasks
- generate a prioritized study plan with a short explanation
- mark tasks as `done` or `not done`
