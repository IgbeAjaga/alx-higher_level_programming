#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter and display the body of response
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    """
    Sends a POST request to the passed
    URL with the email as a parameter
    """
    url = argv[1]
    parameters = {'email': argv[2]}
    data = urllib.parse.urlencode(parameters)
    data = data.encode('ascii')
    call = urllib.request.Request(url, data)
    with urllib.request.urlopen(call) as response:
        front_end = response.read()
        frontend_str = front_end.decode('utf-8')
    print(frontend_str)
