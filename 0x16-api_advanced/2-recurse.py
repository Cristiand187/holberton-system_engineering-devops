#!/usr/bin/python3
"""
The 2-recurse module
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    script that prints a message depending of the number of arguments.
    """
    response = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'
                            .format(subreddit, after),
                            headers={'User-agent': 'Chrome/85.0.4183.102'},
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    if after is None:
        return hot_list

    for i in response.json().get('data').get('children'):
        hot_list.append(i.get('data').get('title'))

    after = response.json().get('data').get('after')
    recurse(subreddit, hot_list, after)
    return(hot_list)
