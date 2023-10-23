#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    response = requests.get(url)
    employee_name = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id)).json().get("name")

    tasks = response.json()
    total_tasks = len(tasks)
    completed_tasks = len([task for task in tasks if task.get('completed')])

    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))
    for task in tasks:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))
