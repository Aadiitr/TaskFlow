# ⚡ TaskFlow

> A modern full-stack productivity and task management web application built with Flask, SQLite, HTML, CSS and JavaScript.

TaskFlow helps users organize daily work, manage priorities, track completion, and monitor productivity through a clean and responsive dashboard.

## 🚀 Features

- 📊 Interactive productivity dashboard
- ✅ Create and complete tasks
- ✏️ Edit existing tasks
- 🗑️ Delete tasks
- 🔎 Search tasks
- 🏷️ Task categories
- 🚨 Priority management
- 📅 Due-date tracking
- 📈 Productivity analytics
- ⚙️ Settings page
- 💾 Persistent SQLite database
- 🌐 REST API backend
- 📱 Responsive web interface

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask
- REST APIs

### Database
- SQLite

### Development Tools
- VS Code
- Git
- GitHub


## 🏗️ Project Architecture

```text
TaskFlow/
│
├── app.py
├── main.py
├── task_manager.py
├── storage.py
├── tasks.json
├── README.md
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   └── routes.py
│
├── templates/
│   ├── index.html
│   ├── tasks.html
│   ├── analytics.html
│   └── settings.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    └── js/
        └── app.js

## 🔌 API Endpoints

TaskFlow provides a RESTful API for managing tasks and retrieving productivity statistics.

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/tasks` | Retrieve all tasks |
| `POST` | `/api/tasks` | Create a new task |
| `PUT` | `/api/tasks/<task_id>` | Update an existing task |
| `PATCH` | `/api/tasks/<task_id>/complete` | Mark a task as completed |
| `DELETE` | `/api/tasks/<task_id>` | Delete a task |
| `GET` | `/api/stats` | Retrieve task statistics |

### Example API Response

```json
{
  "id": 1,
  "title": "Complete project",
  "category": "Project",
  "priority": "High",
  "due_date": "2026-08-15",
  "completed": 0
}



