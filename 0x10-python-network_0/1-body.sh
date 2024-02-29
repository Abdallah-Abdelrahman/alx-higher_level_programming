#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
# shellcheck disable=SC1083

res=$(curl -sw %{http_code} "$1" -o /dev/null)

[ "$res" -eq 200 ] && curl -s "$1" 
