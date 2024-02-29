#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response

stat_code=$(curl -Is "$1" | awk '/HTTP/ {print $2}')

[ "$stat_code" -eq 200 ] && curl -s "$1"
