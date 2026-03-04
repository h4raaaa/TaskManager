from datetime import datetime


class Task:
    """Класс, представляющий задачу"""


    def __init__(self, title: str, description: str = "", priority: str = "средний"):
        """
Конструктор класса Task

Args:
title: Название задачи description: Описание задачи
priority: Приоритет (низкий, средний, высокий)
"""


        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now()
        self.completed_at = None


# Геттеры и сеттеры для title

    @property
    def title(self):
        return self.title


    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and len(new_title.strip()) > 0:
            self.title = new_title
        else:
            raise ValueError("Название задачи не может быть пустым")


# Геттеры и сеттеры для description
    @property
    def description(self):
        return self.description


    @description.setter
    def description(self, new_description):
        if isinstance(new_description, str):
            self.description = new_description
        else:
            raise ValueError("Описание должно быть строкой")


# Геттеры и сеттеры для priority
    @property
    def priority(self):
        return self.priority


    @priority.setter
    def priority(self, new_priority):
        valid_priorities = ["низкий", "средний", "высокий"]
        if new_priority in valid_priorities:
            self.priority = new_priority
        else:
            raise ValueError(f"Приоритет должен быть одним из: {valid_priorities}")

    # Геттер для completed (только чтение)
    @property
    def completed(self):
        return self.completed

    # Геттеры для дат
    @property
    def created_at(self):
        return self.created_at

    @property
    def completed_at(self):
        return self.completed_at

    def mark_completed(self):
        """Отметить задачу как выполненную"""

        if not self.completed:
            self.completed = True
            self.completed_at = datetime.now()
            print(f"Задача '{self.title}' отмечена как выполненная")
        else:
            print(f"Задача '{self.title}' уже была выполнена")

    def str(self):
        """Магический метод для строкового представления задачи"""
        status = "✓" if self.completed else "○"
        priority_symbol = {
            "низкий": "⬇️",
            "средний": "➡️",
            "высокий": "⬆️"
        }.get(self.priority, "")

        return f"{status} [{priority_symbol}] {self.title} - {self.description[:30]}	"

    def get_info(self):
        """Полная информация о задаче"""

        info = f"Задача: {self.title}\n"
        info += f"Описание: {self.description}\n"
        info += f"Приоритет: {self.priority}\n"
        info += f"Создана: {self.created_at.strftime('%d.%m.%Y %H:%M')}\n"

        if self.completed:
            info += f"Выполнена: {self.completed_at.strftime('%d.%m.%Y %H:%M')}"
        else:
            info += "Статус: Не выполнена"
        return info
class ImportantTask(Task):
    """Класс для важных задач (наследник Task)"""


    def __init__(self, title: str, description: str = "", deadline: str = "сегодня"):
        """
    Конструктор важной задачи

    Args:
    title: Название задачи description: Описание deadline: Дедлайн
        """


# Вызываем конструктор родителя с приоритетом "высокий"
        super(). init (title, description, priority="высокий")
        self. deadline = deadline
        self.reminder_set = False
    @property
    def deadline(self):
        return self.deadline


    @deadline.setter
    def deadline(self, new_deadline):
        if isinstance(new_deadline, str) and len(new_deadline.strip()) > 0:
            self.deadline = new_deadline
        else:
            raise ValueError("Дедлайн не может быть пустым")
    def set_reminder(self):
        """Установить напоминание"""
        self.reminder_set = True
        print(f"🔔 Напоминание установлено для задачи '{self.title}'")
# Переопределяем метод   str
    def str(self):
        """Переопределенный метод для важных задач"""
        base_str = super().str()
        reminder = "🔔" if self.reminder_set else "⏰"
        return f"{base_str} [Дедлайн: {self.deadline}] {reminder}"


# Переопределяем метод get_info
    def get_info(self):
        """Расширенная информация для важной задачи"""


        base_info = super().get_info()
        base_info += f"\nДедлайн: {self.deadline}"
        base_info += f"\nНапоминание: {'установлено' if self.reminder_set else 'не установлено'}"
        return base_info