#!/usr/bin/python3
'''function that queries the Reddit API
and prints the titles of the first 10 hot posts listed'''
import requests


def top_ten(subreddit):
    '''top 10 hot posts '''
    url = 'http://reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-agent': 'Chrome/85.0.4183.102'}
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        return

    for i in range(10):
        item = response.json().get('data').get("children")[i]
        print(item.get('data').get('title'))
