#!/bin/bash
# sends a JSON POST request to a URL with the contents of a JSON file
curl -sX POST $1 -H "Content-Type: application/json" -d @$2 -L
