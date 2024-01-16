#!/usr/bin/python3
"""queries the Reddit API and returns titles
    of first 10 hot posts for a given subreddit using recursion"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """queries the Reddit API"""
    hot = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       headers={"User-Agent": "west"},
                       params={"after": after},
                       allow_redirects=False)
    if hot.status_code == 200:
        for data in hot.json().get("data").get("children"):
            children = data.get("data")
            title = children.get("title")
            hot_list.append(title)

        after = hot.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
