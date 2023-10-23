#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = requests.get(f'{url}users/{sys.argv[1]}').json()
    print(f"Employee {user.get('name')} is done with tasks", end="")

    tasks = requests.get(f'{url}todos?userId={sys.argv[1]}').json()
    completed_tasks = [task for task in tasks if task.get('completed')]

    print(f"({len(completed_tasks)}/{len(tasks)}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
