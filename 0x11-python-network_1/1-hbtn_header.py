#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]

        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            header_value = response.info().get('X-Request-Id')
            print(header_value)
