#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
# shellcheck disable=SC1083


curl -s "$1"
