#!/usr/bin/python3
"""Use API to get data and print"""
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user_data = requests.get(url + "users").json()
    todos_data = requests.get(url + "todos", params={"userId": id}).json()

    with open("todo_all_employees.json", "w") as json_file:
        for user in user_data:
            for task in todos_data:
                json.dump({
                    user.get("id"): [{
                        "username": user.get("username"),
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                    }]
                }, json_file)
