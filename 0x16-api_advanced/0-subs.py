#!/usr/bin/python3
'''function that queries the Reddit
API and returns the number of subscribers'''
import requests


def number_of_subscribers(subreddit):
    '''Gets number of reddit subscribers'''
    url = 'http://reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-agent': 'Chrome/85.0.4183.102'}
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
