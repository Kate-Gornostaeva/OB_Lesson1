class Task:
    task_list = []  # Список задач будет храниться как атрибут класса

    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False  # Статус задачи (не выполнено по умолчанию)

    def add_task(self):
        description = input("Введите описание задачи: ")
        deadline = input("Введите срок выполнения задачи: ")
        task = Task(description, deadline)  # Создаем новую задачу
        Task.task_list.append(task)  # Добавляем задачу в список

    def mark_task(self, index):
        if 0 <= index < len(Task.task_list):
            Task.task_list[index].status = True  # Отмечаем задачу как выполненную
        else:
            print("Неверный индекс задачи.")

    def current_tasks(self):
        print("Текущие задачи:")
        for index, task in enumerate(Task.task_list):
            if not task.status:  # Проверяем статус задачи
                print(f"{index + 1}. {task.description} (Срок: {task.deadline})")


# Создаем экземпляр класса для работы с задачами
task_manager = Task("", "")  # Параметры не важны, так как они не используются

# Пример использования методов класса
while True:
    print("\n1. Добавить задачу")
    print("2. Отметить задачу как выполненную")
    print("3. Показать текущие задачи")
    print("4. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        task_manager.add_task()
    elif choice == '2':
        task_index = int(input("Введите номер задачи для отметки как выполненной: ")) - 1
        task_manager.mark_task(task_index)
    elif choice == '3':
        task_manager.current_tasks()
    elif choice == '4':
        break
    else:
        print("Неверный выбор, попробуйте снова.")

