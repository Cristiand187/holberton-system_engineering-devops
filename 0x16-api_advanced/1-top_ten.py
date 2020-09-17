#!/usr/bin/python3
'''function that queries the Reddit
API and returns the number of subscribers'''
import requests


def top_ten(subreddit):
    '''Gets number of reddit subscribers'''
    url = 'http://reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-agent': 'Chrome/85.0.4183.102'}
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        return

    for i in range(10):
        item = response.json().get('data').get("children")[i]
        print(item.get('data').get('title'))
