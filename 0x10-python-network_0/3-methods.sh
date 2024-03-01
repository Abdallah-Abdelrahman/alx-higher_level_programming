#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -I "$1" | awk '{print substr($0, index($0, $2))}'
