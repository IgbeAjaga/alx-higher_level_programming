#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    Takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
    """
    url = 'http://0.0.0.0:5000/search_user'
    call = requests.get(url)
    if len(argv) == 2:
        call = requests.post(url, data={'q': argv[1]})
    else:
        call = requests.post(url, data={'q': ""})
    try:
        if call.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(call.json().get('id'),
                  call.json().get('name')))
    except KeyError:
        print("Not a valid JSON")
