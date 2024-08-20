#!/usr/bin/python3
"""
This script take in employee id and write information about his/her TODo list.
in a csv file
"""
import json
import requests
from sys import argv, exit


def get_employees_todo():
    usernameurl = "https://jsonplaceholder.typicode.com/users/"
    username_r = requests.get(usernameurl)
    if username_r.status_code != 200:
        print("Failed to fetch TODOS for employee_id {}.".format(employee_id))
        return

    usernames = username_r.json()

    dictionary = {}
    filename = "todo_all_employees.json"
    for user in usernames:
        user_id = user['id']
        url = "{}{}/todos/".format(usernameurl, user_id)
        todos = requests.get(url).json()
        lst = []
        for todo in todos:
            lst.append({'username': user['username'],
                        'completed': todo['completed'],
                        'task': todo['title']})
        if user_id in dictionary:
            dictionary[user_id].extend(lst)
        else:
            dictionary[user_id] = lst
    with open(filename, 'w', encoding='utf-8') as fd:
        json.dump(dictionary, fd)


if __name__ == "__main__":
    get_employees_todo()
