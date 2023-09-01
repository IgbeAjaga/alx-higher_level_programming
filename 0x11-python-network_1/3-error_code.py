#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as
a parameter, and displays the body of the response
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    """
    takes in a URL and an email, sends a POST request to the passed
    URL with the email as a parameter, and displays the body of the response
    """
    url = argv[1]
    call = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(call) as response:
            front_end = response.read()
            frontend_str = front_end.decode('utf-8')
            print(frontend_str)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
