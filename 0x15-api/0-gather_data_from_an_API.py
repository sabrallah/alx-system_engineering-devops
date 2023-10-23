#!/usr/bin/python3

"""Script that uses JSONPlaceholder API to get information about employee"""

import requests
import sys

if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    json_o = res.json()

    print(f"Employee {json_o['name']} is done with tasks", end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()

    completed_tasks = [task for task in tasks if task['completed']]

    print("({}/{}):".format(len(completed_tasks), len(tasks)))

    for task in completed_tasks:
        print("\t{}".format(task['title']))
