#!/usr/bin/python3
""" Gather data from an API
"""
import sys
import requests


if __name__ == "__main__":
    user_dit = {'userId': sys.argv[1]}
    data = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params=user_dit)
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        params={'id': 2}).json()[0]['name']
    t_task = len(data.json())
    list_tittle = []
    t_ok = 0
    for item in data.json():
        if item['completed'] is True:
            t_ok += 1
            list_tittle.append(item['title'])
    print("Employee {} is done with tasks({}/{}):".format(name, t_ok, t_task))
    [print("     " + task) for task in list_tittle]
