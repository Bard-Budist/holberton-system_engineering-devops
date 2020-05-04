#!/usr/bin/python3
""" Export to CSV
"""
import csv
import requests
import sys


if __name__ == "__main__":
    user_dit = {'userId': sys.argv[1]}
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        params={'id': 2}).json()[0]['name']
    data = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params=user_dit).json()
    file_csv = open(sys.argv[1] + ".csv", mode='w+')
    write_file = csv.writer(
        file_csv, delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL)
    for item in data:
        write_file.writerow([
            sys.argv[1],
            name,
            item['completed'],
            item['title']
            ])
    file_csv.close()