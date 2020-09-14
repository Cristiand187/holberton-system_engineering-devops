# 0x15. API

## :books: Resources
Read or watch:
* [Friends don’t let friends program in shell script](https://intranet.hbtn.io/rltoken/6isWaTEpGTrwhzCCG5s_Tw)
* [What is an API](https://intranet.hbtn.io/rltoken/13UaAZ1pQKQYY7VVwzJwCQ)
* [What is an API? In English, please](https://intranet.hbtn.io/rltoken/I1nC8rhySGahG3gXYBfDPA)
* [What is a REST API](https://intranet.hbtn.io/rltoken/0KygelrSeZsIujDu-I2a0w)
* [What are microservices](https://intranet.hbtn.io/rltoken/lewYS0z2RuFuiIkIgaCHSA)
* [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](https://intranet.hbtn.io/rltoken/lEisphllQEYAs5yg26Ng0w)

---
## :bulb: Learning Objectives
What you should learn from this project:

* What Bash scripting should not be used for
* What is an API
* What is a REST API
* What are microservices
* What is the CSV format
* What is the JSON format
* Pythonic Package and module name style
* Pythonic Class name style
* Pythonic Variable name style
* Pythonic Function name style
* Pythonic Constant name style
* Significance of CapWords or CamelCase in Python

---
## :computer: Task

### [0. Gather data from an API](./0-gather_data_from_an_API.py)
Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.


### [1. Export to CSV](./1-export_to_CSV.py)
Using what you did in the task #0, extend your Python script to export data in the CSV format.
 * Records all tasks that are owned by this employee
 * Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
 * File name must be: USER_ID.csv


### [2. Export to JSON](./2-export_to_JSON.py)
Using what you did in the task #0, extend your Python script to export data in the JSON format.
 * Records all tasks that are owned by this employee
 * Format must be: { "USER_ID": [ {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, ... ]}
 * File name must be: USER_ID.json


### [3. Dictionary of list of dictionaries](./3-dictionary_of_list_of_dictionaries.py)
Using what you did in the task #0, extend your Python script to export data in the JSON format.
 * Records all tasks from all employees
 * Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
 * File name must be: todo_all_employees.json

---

## Author
* **Cristian David Pineda Vargas** - [Cristiand187](https://github.com/Cristiand187)