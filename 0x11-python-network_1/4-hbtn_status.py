#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using requests
"""
import requests


if __name__ == "__main__":
    """
    Fetches https://intranet.hbtn.io/status using requests
    """
    call = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(call.text)))
    print("\t- content: {}".format(call.text))
