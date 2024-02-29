#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.
curl -I -s -X OPTIONS | awk '/Allow:/ {print $2}'
