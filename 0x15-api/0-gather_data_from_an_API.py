#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress."""
import requests
import sys

user_endpoint = "https://jsonplaceholder.typicode.com/users/"

if __name__ == "__main__":
    """The script must accept an integer as a
    parameter, which is the employee ID"""

    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    user_id = sys.argv[1]

    todos = requests.get(user_endpoint + user_id + '/todos')
    completed = []

    for item in todos.json():
        if item.get('completed') is True:
            completed.append(item)

    user = requests.get(user_endpoint + user_id)

    name = user.json().get('name')
    output = "Employee {} is done with tasks({}/{}):".format(name,
                                                             len(completed),
                                                             len(todos.json()))

    titles = ""
    for item in completed:
        titles += '\n\t{}'.format(item.get('title', ''))

    if not titles:
        output
    output = output + titles

    print(output)
