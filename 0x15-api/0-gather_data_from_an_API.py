#!/usr/bin/python3
"""
This module uses the JSONPlaceholder API to get information about an employee's
TODO list progress given their employee ID.

Usage:
    python3 script.py <employee_id>
"""

import requests
import sys

def get_employee_progress(employee_id):
    """
    Prints the TODO list progress of an employee given their ID.

    Args:
        employee_id (int): The ID of the employee.
    """
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    done_tasks = [task for task in todos_data if task.get('completed') is True]
    total_tasks = len(todos_data)

    print("Employee {} is done with tasks({}/{}):".format(user_data.get('name'), len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: {} <employee_id>'.format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_progress(employee_id)
