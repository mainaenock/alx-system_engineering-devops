#!/usr/bin/python3
"""Recurse it!"""
import requests


def recurse(subreddit, hot_list=[]):
    """Function"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    params = {'limit': 100}
    if len(hot_list) > 0:
        params['after'] = hot_list[-1]['data']['name']
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            children = data['data']['children']
            hot_list.extend(children)
            if len(children) == 100:
                recurse(subreddit, hot_list)
            else:
                return [post['data']['title'] for post in hot_list]
    return None
