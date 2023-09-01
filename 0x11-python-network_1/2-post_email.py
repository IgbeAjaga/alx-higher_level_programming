#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]

        # Create a dictionary with the email parameter
        data = {'email': email}
        data = urllib.parse.urlencode(data)
        data = data.encode('ascii')

        # Create a POST request
        req = urllib.request.Request(url, data)

        # Send the request and get the response
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
