#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
JSON="$(cat "$2")"
curl -s -X POST -H "Content-Type: application/json" -d "$JSON" "$1"
