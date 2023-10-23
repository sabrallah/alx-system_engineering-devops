#!/usr/bin/python3
""" a script that converts data to json """

import json
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    # Divisez la ligne longue en plusieurs lignes
    todos_url = (
        'https://jsonplaceholder.typicode.com'
        '/users/{}/todos'.format(userId)
    )
    todos = requests.get(todos_url)

    name = todos.json()[0].get('username')

    taskList = []

    for task in todos.json():
        taskDict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": name
        }
        taskList.append(taskDict)

    todoUser = {userId: taskList}

    filename = userId + '.json'

    with open(filename, mode="w") as f:
        json.dump(todoUser, f)
