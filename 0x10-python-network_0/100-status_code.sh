#!/bin/bash
# Fetch status code
curl -sw "%{http_code}" -o /dev/null
