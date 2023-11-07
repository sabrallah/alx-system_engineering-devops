#!/usr/bin/python3
"""
Returns the number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'My API script'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.InvalidURL:
        return 0

    json_data = response.json()
    subscribers = json_data.get('data', {}).get('subscribers')

    return subscribers if subscribers else 0
