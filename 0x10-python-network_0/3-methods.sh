#!/bin/bash
# This sends an OPTIONS request to URL and displays allowed HTTP methods
curl -sI "$1" | grep "Allow:" | cut -d' ' -f2-
