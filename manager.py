from task import Task
from datetime import datetime
class TaskManager:
    """Класс для управления списком задач"""


    def init(self, name: str):
        """
Конструктор класса TaskManager

Args:
name: Название менеджера задач
"""
        self.name = name
        self.tasks = []
    @property
    def name(self): return self.name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name.strip()) > 0:
            self.name = new_name
        else:
            raise ValueError("Название не может быть пустым")
    def add_task(self, task: Task):
        """Добавление задачи"""
        if isinstance(task, Task):
            self.tasks.append(task)
            print(f"Задача '{task.title}' добавлена в {self.name}")
        else:
            raise TypeError("Можно добавлять только объекты класса Task")
    def remove_task(self, title: str):
        """Удаление задачи по названию"""
        for i, task in enumerate(self.tasks):
            if task.title.lower() == title.lower():
                removed = self.tasks.pop(i)
                print(f"Задача '{removed.title}' удалена")
                return True
        print(f"Задача '{title}' не найдена")
        return False
    def find_tasks(self, keyword: str):
        """Поиск задач по ключевому слову"""
        found = []
        for task in self.tasks:
            if (keyword.lower() in task.title.lower() or
                keyword.lower() in task.description.lower()):
                found.append(task)
        return found
    def get_tasks_by_priority(self, priority: str):
        """Получение задач по приоритету"""
        return [task for task in self.tasks if task.priority == priority]
    def get_completed_tasks(self):
        """Получение выполненных задач"""
        return [task for task in self.tasks if task.completed]
    def get_pending_tasks(self):
        """Получение невыполненных задач"""
        return [task for task in self.tasks if not task.completed]
    def show_all_tasks(self):
        """Показать все задачи"""
        if not self.tasks:
            print("Список задач пуст")
            return
        print(f"\n=== {self.name} - Все задачи ===\n")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
    def __str__(self):
        """Статистика по задачам"""
        total = len(self.tasks)
        completed = len(self.get_completed_tasks())
        pending = total - completed
        return f"{self.name}: всего {total} задач (выполнено: {completed}, осталось: {pending})"