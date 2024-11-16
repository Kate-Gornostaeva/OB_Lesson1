task_list = []
print("Введите задачу: ")
task = input()
task_list.append(task)
for c, value in enumerate(task_list, 1):
    print(c, value)


