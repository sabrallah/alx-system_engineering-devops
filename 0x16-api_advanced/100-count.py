#!/usr/bin/python3i
"""Module Done"""


import requests


def count_words(subreddit, word_list, after=None):
    """Queries Reddit API recursively for hot post
    titles in a subreddit. Counts occurrences of
    keywords in word_list and prints sorted results.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    params = {'after': after}
    headers = {'User-Agent': 'MyBot'}

    res = requests.get(url, params=params,
                       headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return

    data = res.json()['data']

    titles = [item['data']['title'] for item in data['children']]

    word_counts = {word: 0 for word in word_list}

    for title in titles:
        words = title.lower().split()
        for word in word_list:
            if word in words:
                word_counts[word] += words.count(word)

    if after is None:
        sorted_counts = sorted(word_counts.items(),
                               key=lambda x: (-x[1], x[0]))

        for word, count in sorted_counts:
            if count:
                print('{}: {}'.format(word, count))
        return

    count_words(subreddit, word_list, data['after'])
