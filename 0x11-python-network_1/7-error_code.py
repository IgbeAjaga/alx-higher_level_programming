#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the
body of the response using requests
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    Takes in a URL, sends a request to the URL and displays the
    body of the response using requests
    """
    url = argv[1]
    call = requests.get(url)
    if call.status_code >= 400:
        print("Error code: {}".format(call.status_code))
    else:
        print(call.text)
