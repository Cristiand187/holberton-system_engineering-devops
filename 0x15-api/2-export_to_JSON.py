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
    newd = {}
    with open(filename, "w") as f:
        r_json = todos.json()
        d = [{'task': i.get('title'), 'completed': i.get('completed'),
              'username': name} for i in r_json]
        newd[user_id] = d
        json.dump(newd, f)
