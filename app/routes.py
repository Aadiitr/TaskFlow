from flask import Blueprint, jsonify, request , render_template
from app.database import get_connection

api = Blueprint("api", __name__, url_prefix="/api")


# =========================
# GET ALL TASKS
# =========================

@api.get("/tasks")
def get_tasks():
    connection = get_connection()

    tasks = connection.execute(
        "SELECT * FROM tasks ORDER BY created_at DESC"
    ).fetchall()

    connection.close()

    return jsonify([dict(task) for task in tasks])


# =========================
# CREATE TASK
# =========================

@api.post("/tasks")
def create_task():
    data = request.get_json() or {}

    title = data.get("title", "").strip()
    category = data.get("category", "General")
    priority = data.get("priority", "Medium")
    due_date = data.get("due_date")

    if not title:
        return jsonify({
            "error": "Task title is required"
        }), 400

    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO tasks
        (title, category, priority, due_date)
        VALUES (?, ?, ?, ?)
        """,
        (
            title,
            category,
            priority,
            due_date
        )
    )

    connection.commit()

    task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (cursor.lastrowid,)
    ).fetchone()

    connection.close()

    return jsonify(dict(task)), 201


# =========================
# COMPLETE TASK
# =========================

@api.patch("/tasks/<int:task_id>/complete")
def complete_task(task_id):
    connection = get_connection()

    cursor = connection.execute(
        """
        UPDATE tasks
        SET completed = 1
        WHERE id = ?
        """,
        (task_id,)
    )

    connection.commit()

    connection.close()

    if cursor.rowcount == 0:
        return jsonify({
            "error": "Task not found"
        }), 404

    return jsonify({
        "message": "Task completed"
    })


# =========================
# UPDATE TASK
# =========================

@api.put("/tasks/<int:task_id>")
def update_task(task_id):
    data = request.get_json() or {}

    title = data.get("title", "").strip()
    category = data.get("category", "General")
    priority = data.get("priority", "Medium")
    due_date = data.get("due_date")

    if not title:
        return jsonify({
            "error": "Task title is required"
        }), 400

    connection = get_connection()

    cursor = connection.execute(
        """
        UPDATE tasks
        SET title = ?,
            category = ?,
            priority = ?,
            due_date = ?
        WHERE id = ?
        """,
        (
            title,
            category,
            priority,
            due_date,
            task_id
        )
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()

        return jsonify({
            "error": "Task not found"
        }), 404

    task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    connection.close()

    return jsonify(dict(task))


# =========================
# DELETE TASK
# =========================

@api.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    connection = get_connection()

    cursor = connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()

    connection.close()

    if cursor.rowcount == 0:
        return jsonify({
            "error": "Task not found"
        }), 404

    return jsonify({
        "message": "Task deleted"
    })


# =========================
# STATISTICS
# =========================

@api.get("/stats")
def get_stats():
    connection = get_connection()

    total = connection.execute(
        "SELECT COUNT(*) FROM tasks"
    ).fetchone()[0]

    completed = connection.execute(
        "SELECT COUNT(*) FROM tasks WHERE completed = 1"
    ).fetchone()[0]

    pending = total - completed

    connection.close()

    return jsonify({
        "total": total,
        "completed": completed,
        "pending": pending
    })

