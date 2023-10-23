#!/usr/bin/python3
""" script that use JSONPlaceholder API to get informations about employee """
import csv
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    user = f'{url}users/{userid}'
    res = requests.get(user)
    json_o = res.json()
    name = json_o.get('username')

    todos = f'{url}todos?userId={userid}'
    res = requests.get(todos)
    tasks = res.json()

    filename = f'{userid}.csv'
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in tasks:
            l_task = [userid, name, task.get('completed'), task.get('title')]
            employee_writer.writerow(l_task)
