#!/usr/bin/python3
"""queries the Reddit API and returns the number
    of subscribers for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API"""
    about = requests.get("https://www.reddit.com/r/{}/about.json"
                         .format(subreddit),
                         headers={"User-Agent": "west"},
                         allow_redirects=False)
    if about.status_code == 200:
        return about.json().get("data").get("subscribers")
    else:
        return 0
