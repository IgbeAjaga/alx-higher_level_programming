#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io using requests
"""
import requests


if __name__ == "__main__":
    """
    Fetches https://alx-intranet.hbtn.io using requests
    """
    call = requests.get('https://alx-intranet.hbtn.io')
    print("Body response:")
    print("\t- type: {}".format(type(call.text)))
    print("\t- content: {}".format(call.text))
