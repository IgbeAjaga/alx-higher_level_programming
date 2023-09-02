#!/usr/bin/python3
"""a Python script that fetches a url"""
import urllib.request


if __name__ == "__main__":
    """This fetches https://alx-intranet.hbtn.io/status"""
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as response:
        front_end = response.read()
        frontend_str = front_end.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(front_end)))
    print("\t- content: {}".format(front_end))
    print("\t- utf8 content: {}".format(frontend_str))
