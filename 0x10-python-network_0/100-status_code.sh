#!/bin/bash
# shellcheck disable=SC1083
curl -sw %{http_code} localhost -o /dev/null; echo ''
