import json
from model import Task

task_list = []

def add_task(new_task):
    task_list.append(new_task)

def show_tasks():
    for task in task_list:
        print(task)

def del_task(task_to_delete):
    if task_to_delete in task_list:
        task_list.remove(task_to_delete)
        return True
    else:
        return False

def edit_task(task_to_edit,new_task):
    if task_to_edit in task_list:
        index = task_list.index(task_to_edit)
        task_list[index] = new_task
        return True
    else:
        return False

def list_of_dict(): 
    formatted_tasks = []
    formatted_tasks = [task.to_dict() for task in task_list]
    return formatted_tasks

def save_task(file):
    with open(file, "w") as f:
        json.dump(list_of_dict(),f,indent=4)