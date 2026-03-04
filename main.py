from task import Task


def main():
    """Главная функция для тестирования"""


    print("=== СОЗДАНИЕ ЗАДАЧ ===\n")

# Создаем несколько задач
    task1 = Task(
        "Купить продукты", "Молоко, хлеб, яйца, сыр", "высокий"
    )

    task2 = Task(
        "Сделать домашнее задание", "Решить задачи по математике", "средний"
)

    task3 = Task(
        "Позвонить родителям", priority="низкий"
)

# Выводим краткую информацию print("Краткая информация:") print(task1)
    print(task2)
    print(task3)

    print("\n=== ТЕСТИРОВАНИЕ МЕТОДОВ ===\n")

# Изменяем приоритет
    print(f"Старый приоритет task1: {task1.priority}")
    task1.priority = "средний"
    print(f"Новый приоритет task1: {task1.priority}")

# Отмечаем задачу выполненной
    task2.mark_completed()
    task2.mark_completed()  # Попытка отметить повторно

    print("\n=== ПОЛНАЯ ИНФОРМАЦИЯ ===\n")

    print(task1.get_info())
    print("\n" + "=" * 40 + "\n")
    print(task2.get_info())

    print("\n=== ПРОВЕРКА ВАЛИДАЦИИ ===\n")

# Пробуем установить некорректный приоритет
    try:
        task3.priority = "очень высокий"
    except ValueError as e:
        print(f"Ошибка: {e}")

# Пробуем установить пустое название
    try:
        task3.title = ""
    except ValueError as e:
        print(f"Ошибка: {e}")

    if name == " main ": main()