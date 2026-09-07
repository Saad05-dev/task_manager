from model import Task
from collection import add_task,save_tasks,get_task,get_tasks,list_from_dict,list_of_dict,load_tasks,del_task,edit_task
import os

file = "../docs/data.json"

print("===============================================")
print("             Task Manager CLI App              ")
print()
print()
print()
print("Welcome!")


if not os.path.exists(file):
    open(file, "w").close()
if os.path.getsize(file) == 0:
    print("File is empty")
else:
    load_tasks(file)


task1 = Task(1, "Complete project documentation")
task2 = Task(2, "Review pull requests")
task3 = Task(3, "Fix bug in login module", status="in-progress")
task4 = Task(4, "Update database schema", status="done")
task5 = Task(5, "Write unit tests for API")

add_task(task1)
add_task(task2)
add_task(task3)
add_task(task4)
add_task(task5)

i = 0
for tasks in get_tasks():
    print("----------------")
    print(f"Task number {i+1}")
    print(f"ID: {tasks.id}")
    print(f"Description: {tasks.description}")
    print(f"Status: {tasks.status}")
    print(f"Created at: {tasks.createdAt}")
    print(f"Last updated: {tasks.updatedAt}")
    print("----------------")
    i += 1

save_tasks(file)