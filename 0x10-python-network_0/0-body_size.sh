#!/bin/bash
# This script sends a request to URL and displays the size the response body
curl -sI "$1" | grep -i "Content-Length:" | awk '{print $2}'
