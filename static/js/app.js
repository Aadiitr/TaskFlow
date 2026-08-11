const modal = document.getElementById("taskModal");
const openModalBtn = document.getElementById("openModalBtn");
const closeModalBtn = document.getElementById("closeModalBtn");
const cancelBtn = document.getElementById("cancelBtn");
const taskForm = document.getElementById("taskForm");

const taskList = document.querySelector(".task-list");


let tasks = [];


/* =========================
   MODAL
   ========================= */

function openModal() {
    modal.classList.add("show");
    document.getElementById("title").focus();
}


function closeModal() {
    modal.classList.remove("show");
    taskForm.reset();
}


openModalBtn.addEventListener("click", openModal);

closeModalBtn.addEventListener("click", closeModal);

cancelBtn.addEventListener("click", closeModal);


modal.addEventListener("click", (event) => {
    if (event.target === modal) {
        closeModal();
    }
});


/* =========================
   LOAD TASKS
   ========================= */

async function loadTasks() {

    try {

        const response = await fetch("/api/tasks");

        if (!response.ok) {
            throw new Error("Failed to load tasks");
        }

        tasks = await response.json();

        renderTasks();
        await loadStats();

    } catch (error) {

        console.error("Error loading tasks:", error);

    }
}


/* =========================
   RENDER TASKS
   ========================= */

function renderTasks() {

    taskList.innerHTML = "";

    if (tasks.length === 0) {

        taskList.innerHTML = `
            <div class="empty-state">
                <div class="empty-icon">📝</div>
                <h3>No tasks yet</h3>
                <p>Create your first task to get started.</p>
            </div>
        `;

        return;
    }


    tasks.forEach((task) => {

        const taskElement = document.createElement("div");

        taskElement.className = "task";

        const statusClass = task.completed
            ? "completed-task"
            : "";

        const statusIcon = task.completed
            ? "✓"
            : "○";


        taskElement.innerHTML = `

            <div class="task-info">

                <button
                    class="complete-btn ${statusClass}"
                    onclick="completeTask(${task.id})"
                    title="Mark complete"
                >
                    ${statusIcon}
                </button>

                <div>

                    <div class="task-title ${statusClass}">
                        ${escapeHtml(task.title)}
                    </div>

                    <div class="task-meta">
                        ${escapeHtml(task.category)}
                        •
                        ${task.due_date || "No due date"}
                    </div>

                </div>

            </div>


            <div class="task-actions">

                <span class="priority ${task.priority.toLowerCase()}">
                    ${escapeHtml(task.priority.toUpperCase())}
                </span>

                <button
                    class="delete-btn"
                    onclick="deleteTask(${task.id})"
                    title="Delete task"
                >
                    🗑
                </button>

            </div>

        `;


        taskList.appendChild(taskElement);

    });
}


/* =========================
   ADD TASK
   ========================= */

taskForm.addEventListener("submit", async (event) => {

    event.preventDefault();


    const taskData = {

        title: document
            .getElementById("title")
            .value
            .trim(),

        category: document
            .getElementById("category")
            .value,

        priority: document
            .getElementById("priority")
            .value,

        due_date: document
            .getElementById("dueDate")
            .value || null
    };


    try {

        const response = await fetch("/api/tasks", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(taskData)

        });


        const result = await response.json();


        if (!response.ok) {
            throw new Error(
                result.error || "Failed to create task"
            );
        }


        closeModal();

        await loadTasks();

    } catch (error) {

        console.error(error);

        alert(error.message);

    }

});


/* =========================
   COMPLETE TASK
   ========================= */

async function completeTask(taskId) {

    try {

        const response = await fetch(
            `/api/tasks/${taskId}/complete`,
            {
                method: "PATCH"
            }
        );


        if (!response.ok) {

            const result = await response.json();

            throw new Error(
                result.error || "Failed to complete task"
            );
        }


        await loadTasks();

    } catch (error) {

        console.error(error);

        alert(error.message);

    }
}


/* =========================
   DELETE TASK
   ========================= */

async function deleteTask(taskId) {

    const confirmed = confirm(
        "Are you sure you want to delete this task?"
    );


    if (!confirmed) {
        return;
    }


    try {

        const response = await fetch(
            `/api/tasks/${taskId}`,
            {
                method: "DELETE"
            }
        );


        if (!response.ok) {

            const result = await response.json();

            throw new Error(
                result.error || "Failed to delete task"
            );
        }


        await loadTasks();

    } catch (error) {

        console.error(error);

        alert(error.message);

    }
}


/* =========================
   STATISTICS
   ========================= */

async function loadStats() {

    try {

        const response = await fetch("/api/stats");

        if (!response.ok) {
            throw new Error("Failed to load statistics");
        }

        const stats = await response.json();


        document.getElementById(
            "totalTasks"
        ).textContent = stats.total;


        document.getElementById(
            "completedTasks"
        ).textContent = stats.completed;


        document.getElementById(
            "pendingTasks"
        ).textContent = stats.pending;

    } catch (error) {

        console.error(
            "Error loading statistics:",
            error
        );

    }
}


/* =========================
   SECURITY HELPER
   ========================= */

function escapeHtml(value) {

    const div = document.createElement("div");

    div.textContent = value ?? "";

    return div.innerHTML;
}


/* =========================
   INITIAL LOAD
   ========================= */

loadTasks();
async function loadStats() {
    try {
        const response = await fetch("/api/stats");
        const stats = await response.json();

        document.getElementById("totalTasks").textContent = stats.total;
        document.getElementById("completedTasks").textContent = stats.completed;
        document.getElementById("pendingTasks").textContent = stats.pending;

    } catch (error) {
        console.error("Failed to load statistics:", error);
    }
}

loadStats();