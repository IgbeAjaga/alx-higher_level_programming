#!/bin/bash
# This sends a POST request to a URL with specified parameters and displays response
curl -sX POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
