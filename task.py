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

    def save_to_file(self, filename: str = "tasks.json"):
        """Сохраняет задачи в JSON файл"""
        try:
            data = []
            for task in self.tasks:
                task_data = {
                    'type': 'Important' if isinstance(task, ImportantTask) else 'Regular',
                    'title': task.title,
                    'description': task.description,
                    'priority': task.priority,
                    'completed': task.completed,
                    'created_at': task.created_at.isoformat() if task.created_at else None,
                    'completed_at': task.completed_at.isoformat() if task.completed_at else None
                }

                # Добавляем специфичные для ImportantTask поля
                if isinstance(task, ImportantTask):
                    task_data['deadline'] = task.deadline.isoformat() if task.deadline else None

                data.append(task_data)

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            print(f"✓ Задачи сохранены в файл {filename}")

        except PermissionError:
            print(f"✗ Нет прав для записи в файл {filename}")
        except Exception as e:
            print(f"✗ Ошибка при сохранении: {e}")

    @classmethod
    def load_from_file(cls, name: str, filename: str = "tasks.json"):
        """
        Загружает задачи из JSON файла

        Args:
            name: Название менеджера задач
            filename: Имя файла
        """
        manager = cls(name)

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            for item in data:
                try:
                    if item['type'] == 'Important':
                        task = ImportantTask(
                            item['title'],
                            item['description'],
                            priority=item.get('priority', 1),
                            deadline=datetime.fromisoformat(item['deadline']) if item.get('deadline') else None
                        )
                    else:
                        task = Task(
                            item['title'],
                            item['description'],
                            priority=item.get('priority', 1)
                        )

                    # Восстанавливаем состояние
                    if item.get('completed'):
                        task.completed = True
                    if item.get('completed_at'):
                        task.completed_at = datetime.fromisoformat(item['completed_at'])
                    if item.get('created_at'):
                        task.created_at = datetime.fromisoformat(item['created_at'])

                    manager.tasks.append(task)

                except Exception as e:
                    print(f"✗ Ошибка при загрузке задачи {item.get('title', 'unknown')}: {e}")
                    continue

            print(f"✓ Загружено {len(manager)} задач из файла {filename}")

        except FileNotFoundError:
            print(f"✗ Файл {filename} не найден")
        except json.JSONDecodeError:
            print(f"✗ Ошибка формата JSON в файле {filename}")
        except Exception as e:
            print(f"✗ Ошибка при загрузке: {e}")

        return manager
class Task:
    # ... (предыдущий код) ...

    @staticmethod
    def validate_priority(priority):
        """Проверяет корректность приоритета"""
        valid_priorities = ["низкий", "средний", "высокий"]
        return priority in valid_priorities

    @staticmethod
    def get_priority_emoji(priority):
        """Возвращает эмодзи для приоритета"""
        emojis = {
            "низкий": "⬇️",
            "средний": "➡️",
            "высокий": "⬆️"
        }
        return emojis.get(priority, "❓")

    @classmethod
    def create_from_string(cls, task_string: str):
        """
        Создает задачу из строки формата: "Название | Описание | Приоритет"

        Args:
            task_string: Строка в формате "Название | Описание | Приоритет"

        Returns:
            Экземпляр Task или None в случае ошибки
        """
        try:
            parts = task_string.split('|')
            title = parts[0].strip()
            description = parts[1].strip() if len(parts) > 1 else ""
            priority = parts[2].strip() if len(parts) > 2 else "средний"

            if not cls.validate_priority(priority):
                print(f"Предупреждение: Некорректный приоритет '{priority}'. Используется 'средний'.")
                priority = "средний"

            return cls(title, description, priority)

        except IndexError as e:
            print(f"Ошибка формата строки: недостаточно частей в строке '{task_string}'. {e}")
            return None
        except Exception as e:
            print(f"Ошибка создания задачи из строки: {e}")
            return None
