import json
from model import Task

task_list = []

def add_task(new_task):
    for task in task_list:
        if task.id == new_task.id:
            return False
    task_list.append(new_task)
    return True

def get_tasks():
    return task_list

def get_task(task_id):
    for task in task_list:
        if task.id == task_id:
            return task

    return None
             
def del_task(task_id):
    for task in task_list:
        if task.id == task_id:
            task_list.remove(task)
            return True
        
    return False

def edit_task(task_to_edit,new_task):
    for task in task_list:
        if task.id == task_to_edit.id:
            task_to_edit.change_description(new_task.description) 
            task_to_edit.change_status(new_task.status) 
            return True
    return False

def list_of_dict(): 
    formatted_tasks = []
    formatted_tasks = [task.to_dict() for task in task_list]
    return formatted_tasks

def list_from_dict(dicts):
    for entry in dicts:
        task = Task.from_dict(entry)
        task_list.append(task)

def save_tasks(file):
    with open(file, "w") as f:
        json.dump(list_of_dict(),f,indent=4)

def load_tasks(file):
    try:
        with open(file, "r") as f:
            dicts = json.load(f)
            list_from_dict(dicts)
        return True
    except FileNotFoundError:
        return False