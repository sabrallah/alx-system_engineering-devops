#!/usr/bin/python3
""" Script converts data to json """

import json
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    # use one request to get todos of secific user
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(userId))

    # no need to do another request to get user
    name = todos.json()[0].get('username')

    taskList = []

    # no need to check userId because we are already filtrate todos per userId
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
