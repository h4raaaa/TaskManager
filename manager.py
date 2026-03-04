import json
from datetime import datetime
from task import Task, ImportantTask


class TaskManager:
    """Класс для управления списком задач"""

    # ... (предыдущий код остается без изменений) ...

    def add_task(self, task: Task):
        """Добавление задачи с обработкой ошибок"""
        try:
            if not isinstance(task, Task):
                raise TypeError("Можно добавлять только объекты класса Task")

            # Проверяем, нет ли уже задачи с таким названием
            for existing_task in self.tasks:
                if existing_task.title.lower() == task.title.lower():
                    raise ValueError(f"Задача '{task.title}' уже существует")

            self.tasks.append(task)
            print(f"✓ Задача '{task.title}' добавлена в {self.name}")

        except TypeError as e:
            print(f"✗ Ошибка типа: {e}")
        except ValueError as e:
            print(f"✗ Ошибка значения: {e}")
        except Exception as e:
            print(f"✗ Непредвиденная ошибка: {e}")

    def get_task_by_index(self, index: int):
        """Получение задачи по индексу с обработкой ошибок"""
        try:
            if not isinstance(index, int):
                raise TypeError("Индекс должен быть целым числом")

            if index < 0:
                raise IndexError("Индекс не может быть отрицательным")

            return self.tasks[index]

        except IndexError:
            print(f"✗ Задача с индексом {index} не найдена")
            return None
        except TypeError as e:
            print(f"✗ {e}")
            return None

    # Магические методы для удобства
    def __len__(self):
        """Возвращает количество задач"""
        return len(self.tasks)

    def __getitem__(self, index):
        """Позволяет обращаться по индексу: manager[0]"""
        return self.get_task_by_index(index)

    def __contains__(self, title):
        """Позволяет использовать 'in': if 'Купить' in manager"""
        return any(task.title.lower() == title.lower() for task in self.tasks)