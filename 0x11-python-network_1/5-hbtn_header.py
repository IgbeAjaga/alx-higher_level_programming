#!/usr/bin/python3
"""
Displays the value of the X-Request-Id
variable found in the header of the response using requests
"""
import requests
from sys import argv

if __name__ == "__main__":
    """
    Takes in a URL, sends a request to the URL, and displays
    the value of the X-Request-Id variable found in the header
    of the response using requests
    """
    call = requests.get(argv[1])
    try:
        call_id = call.headers['X-Request-Id']
        print(call_id)
    except KeyError:
        pass
