#!/usr/bin/python3
"""Use API to get data and print"""
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user_data = requests.get(url + "users/{}".format(id)).json()
    todos_data = requests.get(url + "todos", params={"userId": id}).json()

    with open("{}.json".format(id), "w") as json_file:
        tasks = []
        for task in todos_data:
            tasks.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user_data.get("username")
            })

        save_format = {id: tasks}
        json.dump(save_format, json_file)
