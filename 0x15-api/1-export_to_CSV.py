#!/usr/bin/python3
"""
This script take in employee id and write information about his/her TODo list.
in a csv file
"""
import csv
import requests
from sys import argv, exit
from urllib.parse import urlparse


def get_employees_todo(employee_id):
    usernameurl = "https://jsonplaceholder.typicode.com/users/{}".format(
            employee_id
        )
    url = "{}/todos".format(usernameurl)
    response = requests.get(url)
    username_r = requests.get(usernameurl)
    if response.status_code != 200 and username_r.status_code != 200:
        print("Failed to fetch TODOS for employee_id {}.".format(employee_id))
        return

    username = username_r.json()
    todos = response.json()

    filename = "{}.csv".format(employee_id)
    with open(filename, 'w', newline='') as fd:
        csv_writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
        for todo in todos:
            csv_writer.writerow([str(employee_id),
                                username['username'],
                                str(todo['completed']),
                                todo['title']])


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: pythonfilename employee_id")
        exit(1)

    try:
        employee_id = int(argv[1])
    except ValueError:
        print("Employee_id must be an integer")
    get_employees_todo(employee_id)
