# Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных
# задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False

task_list = []

    def add_task(self):
        print("Введите задачу: ")
        self.task_list.append ()


    def mark_task (self):
        self.status = True

    def current_tasks (self):
        for c, value in enumerate(self.task_list, 1):
            print(c, value)



