#!/bin/bash
# This script sends a GET request to a URL with a specific header
curl -sH "X-School-User-Id: 98" "$1"
