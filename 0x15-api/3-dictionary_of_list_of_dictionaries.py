#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress."""
import requests
import sys
import json


if __name__ == "__main__":
    """The script must accept an integer as a
    parameter, which is the employee ID"""

    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit(1)
    user_id = sys.argv[1]
    filename = user_id + ".json"

    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id))

    name = (user.json().get('username'))
    with open(filename, "w") as f:
        d = {j.get("id"): [{'task': i.get('title'),
                            'completed': i.get('completed'),
                           'username': j.get('username')} for i in todos.json()
                           if j.get("id") == i.get('userId')]
             for j in user.json()}
        json.dump(d, f)
