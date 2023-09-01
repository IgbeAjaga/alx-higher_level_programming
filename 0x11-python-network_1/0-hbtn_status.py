#!/usr/bin/python3
"""A Python script that fetches a URL"""
import urllib.request

if __name__ == "__main__":
    # Fetch the URL
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        front_end = response.read()
        frontend_str = front_end.decode('utf-8')

    # Print the response information
    print("Body response:")
    print("\t- type: {}".format(type(front_end)))
    print("\t- content: {}".format(front_end))
    print("\t- utf8 content: {}".format(frontend_str))
