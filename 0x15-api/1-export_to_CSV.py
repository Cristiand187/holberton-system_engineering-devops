#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress."""
import requests
import sys
import csv

user_endpoint = "https://jsonplaceholder.typicode.com/users/"

if __name__ == "__main__":
    """The script must accept an integer as a
    parameter, which is the employee ID"""

    user_id = sys.argv[1]
    filename = user_id + ".csv"

    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id))

    name = (user.json().get('username'))

    with open(filename, "w") as f:
        r_json = todos.json()
        for i in r_json:
            if i.get('userId') == int(user_id):
                w = csv.writer(f, quoting=csv.QUOTE_ALL)
                w.writerow([i.get('userId'), name,
                            i.get('completed'), i.get('title')])
