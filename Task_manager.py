# Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных
# задач и вывода списка текущих (не выполненных) задач.

class Task():
    task_list = []
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False


    def add_task(self):
        description = input ("Введите задачу: ")
        deadline = input("Срок выполнения задачи:  ")
        task = Task(description, deadline)
        Task.task_list.append (task)


    def mark_task (self, index):
        if index >=0 and index <= len(Task.task_list):
            Task.task_list[index].status = True
        else:
            print("Неверный индекс задачи")

    def current_tasks (self):
        for index, task in enumerate(Task.task_list):
            if not task.status:
                print(f"{index+1}. {task.description}. Выполнить {task.deadline}")

task_manager = Task('', '')
while True:
    print("\nВаш список задач:")
    task_manager.current_tasks()
    print("\nВыберите действие:")
    print("1 - добавить задачу")
    print("2 - отметить задачу как выполненную")
    print("3 - завершить работу со списком задач")
    user_choice = int(input(":"))

    if user_choice == 1:
        task_manager.add_task()
    elif user_choice == 2:
        task_index = int(input("Введите индекс выполненной задачи:  ")) - 1
        task_manager.mark_task(task_index)
    elif user_choice == 3:
        break
    else:
        print("Неверный выбор. Введите номер действия 1, 2 или 3")





