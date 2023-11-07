#!/usr/bin/python3
"""
    Uses Reddit API to get all hot posts
"""


def recurse(subreddit, hot_list=[]):
    """
    Recursive function to query the Reddit API and retrieve hot article titles.
    """
    import requests

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data.get("data", {}).get("children", [])
        for child in children:
            title = child.get("data", {}).get("title")
            hot_list.append(title)
        after = data.get("data", {}).get("after")
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
