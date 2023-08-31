#!/bin/bash
# This script sends a request to a URL and displays size of response body

curl -sI "$1" | grep -i "Content-Length:" | awk '{print $2}'
