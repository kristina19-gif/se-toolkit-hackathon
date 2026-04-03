const apiBaseUrl = "http://127.0.0.1:8000";

const taskForm = document.getElementById("task-form");
const taskList = document.getElementById("task-list");
const planList = document.getElementById("plan-list");
const planExplanation = document.getElementById("plan-explanation");
const loadTasksButton = document.getElementById("load-tasks");
const generatePlanButton = document.getElementById("generate-plan");

async function fetchTasks() {
    const response = await fetch(`${apiBaseUrl}/tasks`);
    const tasks = await response.json();

    taskList.innerHTML = "";

    for (const task of tasks) {
        const item = document.createElement("li");
        item.textContent = `${task.title} | importance: ${task.importance} | effort: ${task.effort} | done: ${task.done}`;
        taskList.appendChild(item);
    }
}

async function fetchPlan() {
    const response = await fetch(`${apiBaseUrl}/plan`);
    const plan = await response.json();

    planList.innerHTML = "";
    planExplanation.textContent = plan.explanation;

    for (const task of plan.tasks) {
        const item = document.createElement("li");
        item.textContent = `${task.title} | importance: ${task.importance} | effort: ${task.effort}`;
        planList.appendChild(item);
    }
}

taskForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const formData = new FormData(taskForm);
    const payload = {
        title: String(formData.get("title")),
        importance: Number(formData.get("importance")),
        effort: Number(formData.get("effort")),
    };

    await fetch(`${apiBaseUrl}/tasks`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
    });

    taskForm.reset();
    await fetchTasks();
    await fetchPlan();
});

loadTasksButton.addEventListener("click", async () => {
    await fetchTasks();
});

generatePlanButton.addEventListener("click", async () => {
    await fetchPlan();
});
