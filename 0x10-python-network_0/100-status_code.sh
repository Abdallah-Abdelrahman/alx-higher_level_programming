#!/bin/bash
# Fetch status code
curl -sw "%{http_code}\n" -o /dev/null
