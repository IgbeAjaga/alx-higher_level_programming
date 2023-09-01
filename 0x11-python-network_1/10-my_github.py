#!/usr/bin/python3
"""
Takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    Takes your Github credentials (username and password)
    and uses the Github API to display your id
    """
    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'
    call = requests.get(url, auth=(username, password))
    try:
        print(call.json().get('id'))
    except:
        pass
