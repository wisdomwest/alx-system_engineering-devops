#!/usr/bin/python3
"""queries the Reddit API and returns the number
    of subscribers for a given subreddit"""

import requests
from requests.exceptions import HTTPError


def number_of_subscribers(subreddit):
    """queries the Reddit API"""
    about = requests.get("https://www.reddit.com/r/{}/about.json"
                         .format(subreddit),
                         headers={"User-Agent": "west"},
                         allow_redirects=False)
    if about.status_code == 404:
        return 0

    return about.json().get("data").get("subscribers")
