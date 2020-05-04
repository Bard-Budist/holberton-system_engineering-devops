#!/usr/bin/python3
""" Export to CSV
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    user_dit = {'userId': sys.argv[1]}
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        params={'id': sys.argv[1]}).json()[0]['username']
    data = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params=user_dit).json()
    file_json = open(sys.argv[1] + ".json", mode='w+')
    content = [{
        'task': item['title'],
        'completed': item['completed'],
        'username': name} for item in data]
    json.dump({str(sys.argv[1]): content}, file_json)
    file_json.close()
