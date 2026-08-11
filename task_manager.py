from storage import load_tasks, save_tasks


class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, title):
        task_id = max((task["id"] for task in self.tasks), default=0) + 1

        task = {
            "id": task_id,
            "title": title,
            "completed": False
        }

        self.tasks.append(task)
        save_tasks(self.tasks)
        return task

    def get_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                save_tasks(self.tasks)
                return True

        return False

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                save_tasks(self.tasks)
                return True

        return False

    def search_tasks(self, keyword):
        keyword = keyword.lower()

        return [
            task
            for task in self.tasks
            if keyword in task["title"].lower()
        ]