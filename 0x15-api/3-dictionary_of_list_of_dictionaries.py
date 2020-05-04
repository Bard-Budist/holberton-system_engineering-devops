#!/usr/bin/python3
""" Export to CSV
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    content = {}
    count = 1
    number_user = requests.get(
        "https://jsonplaceholder.typicode.com/users")
    for employer in range(0, len(number_user.json())):
        data = requests.get(
            "https://jsonplaceholder.typicode.com/todos",
            params={'userId': number_user.json()[employer]['id']}).json()
        content[str(count)] = [{
            'username': number_user.json()[employer]['username'],
            'task': itemp['title'],
            'completed': itemp['completed']
        } for itemp in data]
        count += 1
    file_json = open("todo_all_employees.json", mode="w+")
    json.dump(content, file_json)
    file_json.close()
