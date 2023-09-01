#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response using requests
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    Takes in a URL and an email, sends a POST request to the passed URL with
    the email as a parameter, displays the body of response using requests
    """
    url = argv[1]
    call = requests.post(url, data={'email': argv[2]})
    print(call.text)
