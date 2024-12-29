import argparse
import json
import os
from datetime import datetime

tasks_file = 'tasks.json'

def load_tasks():
    if not os.path.exists(tasks_file):
        return []
    with open (tasks_file, 'r') as file:
        return json.load(file)
    
def save_tasks(tasks):
    with open(tasks_file, 'w') as file:
        json.dump(tasks, file, indent=4)
        
def add_task(description):
    tasks = load_tasks()
    new_task = {
        'id': len(tasks) + 1,
        'description': description,
        'status': 'todo',
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat(),
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f'Task added succesfully (ID: {new_task["id"]})')
    
def update_task(task_id, description):
    tasks = load_tasks
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updated_at'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} updated succesfully')
            return
    print(f'Task with ID {task_id} not found')
    
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f'Task {task_id} deleted succesfully')
    
def change_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updated_at'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} updated succesfully as {status}')
            return
    print(f'Task with ID {task_id} not found')
    
def list_tasks(status=None):
    tasks = load_tasks()
    filtered_tasks = tasks if status is None else [task for task in tasks if task["status"] == status]
    for task in filtered_tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
        
def main():
    parser = argparse.ArgumentParser(description='Task Tracker CLI')
    subparsers = parser.add_subparsers(dest='command', required=True)
    
    subparsers.add_parser('add').add_argument('description', type=str, help='Task description')
    
    update_parser = subparsers.add_parser('update')
    update_parser.add_argument('id', type=int, help='ID of the task to update')
    update_parser.add_argument('description', type=str, help='New description for the task')
    
    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('id', type=int, help='ID of the task to delete')
    
    mark_parser = subparsers.add_parser('mark')
    mark_parser.add_argument('status', choices={'todo', 'in-progress', 'done'}, help='New status for the task')
    mark_parser.add_argument('id', type=int, help='ID of the task to mark')
    
    list_parser = subparsers.add_parser('list')
    list_parser.add_argument('status', nargs='?', choices=['todo', 'in-progress', 'done'], help='Filter tasks by status')
    
    args = parser.parse_args()
    
    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'update':
        update_task(args.id, args.description)
    elif args.command == 'delete':
        delete_task(args.id)
    elif args.command == 'mark':
        change_status(args.id, args.status)
    elif args.command == 'list':
        list_tasks(args.status)
        
if __name__ == "__main__":
    main()
    
    
