#!/usr/bin/python3
"""
Exports data in the JSON format
"""

import json
import requests


def main():
    """
    Main function to run the script
    """
    with requests.Session() as session:
        users = session.get(
            "https://jsonplaceholder.typicode.com/users").json()
        todos = session.get(
            'https://jsonplaceholder.typicode.com/todos').json()

    todo_all = {}
    for user in users:
        task_list = [
            {
                "username": user.get('username'),
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            for task in todos if task.get('userId') == user.get('id')
        ]
        todo_all[user.get('id')] = task_list

    with open('todo_all_employees.json', mode='w') as file:
        json.dump(todo_all, file)


if __name__ == "__main__":
    main()
