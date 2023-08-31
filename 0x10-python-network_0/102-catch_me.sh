#!/bin/bash
# makes a request that causes the server to respond with "You got me!"
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" "$1/catch_me"
