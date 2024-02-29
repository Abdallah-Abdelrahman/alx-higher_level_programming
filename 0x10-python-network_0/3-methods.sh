#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.
curl -sIX OPTIONS "$1" | awk '/allow-methods/ {print $2}'
