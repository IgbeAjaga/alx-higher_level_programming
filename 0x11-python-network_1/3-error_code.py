#!/usr/bin/python3
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]

        try:
            with urllib.request.urlopen(url) as response:
                body = response.read().decode('utf-8')
                print(body)
        except urllib.error.HTTPError as e:
            print(f"Error code: {e.code}")
