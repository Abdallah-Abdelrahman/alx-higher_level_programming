#!/bin/bash
# shellcheck disable=SC1083
curl -sw %{http_code} "$1" -o /dev/null; echo ''
