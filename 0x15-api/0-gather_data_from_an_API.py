#!/usr/bin/python3
"""Use API to get data and print"""
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user_data = requests.get(url + "users/{}".format(id)).json()
    todos_data = requests.get(url + "todos", params={"userId": id}).json()

    completed = []
    for task in todos_data:
        if task.get("completed") is True:
            completed.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get("name"), len(completed), len(todos_data)))

    for i in completed:
        print("\t {}".format(i))
