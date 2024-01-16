#!/usr/bin/python3
"""queries the Reddit API and returns titles 
    of first 10 hot posts for a given subreddit"""

import requests


def top_ten(subreddit):
    """queries the Reddit API"""
    hot = requests.get("https://www.reddit.com/r/{}/hot.json"
                         .format(subreddit),
                         headers={"User-Agent": "west"},
                         params={"limit": 10},
                         allow_redirects=False)
    if hot.status_code == 200:
        for data in hot.json().get("data").get("children"):
            children = data.get("data")
            title = children.get("title")
            print(title)
    else:
        print(None)
