#!/usr/bin/python3
"""Use API to get data and export to CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user_data = requests.get(url + "users/{}".format(id)).json()
    todos_data = requests.get(url + "todos", params={"userId": id}).json()

    with open("{}.csv".format(id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            writer.writerow([
                id,
                user_data.get("username"),
                task.get("completed"),
                task.get("title")
            ])
