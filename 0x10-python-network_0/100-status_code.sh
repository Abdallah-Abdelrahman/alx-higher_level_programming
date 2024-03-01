#!/bin/bash
# Fetch status code
curl -s -w "%{http_code}" -o /dev/null "$1"
