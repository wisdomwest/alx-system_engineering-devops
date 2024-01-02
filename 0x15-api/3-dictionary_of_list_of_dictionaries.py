#!/usr/bin/python3
"""Use API to get data and print"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_data = requests.get(url + "users").json()
    id_tasks = {}

    with open("todo_all_employees.json", "w") as json_file:
        for user in user_data:
            id = user.get("id")
            todos_data = requests.get(
                url + "todos", params={"userId": id}).json()
            tasks = []
            for task in todos_data:
                tasks.append({
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

            id_tasks[id] = tasks

        json.dump(id_tasks, json_file)
