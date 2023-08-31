#!/bin/bash
# sends a JSON POST request to a URL with the contents of a JSON file
if [ -f "$2" ]; then
    curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
else
    echo "File not found: $2"
fi
