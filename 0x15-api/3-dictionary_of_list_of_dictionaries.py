#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress."""
import requests
import sys
import json


if __name__ == "__main__":
    """The script must accept an integer as a
    parameter, which is the employee ID"""

    filename = "todo_all_employees.json"

    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    user = requests.get('https://jsonplaceholder.typicode.com/users/')

    with open(filename, "w") as f:
        d = {j.get("id"): [{'task': i.get('title'),
                            'completed': i.get('completed'),
                           'username': j.get('username')} for i in todos.json()
                           if j.get("id") == i.get('userId')]
             for j in user.json()}
        json.dump(d, f)
