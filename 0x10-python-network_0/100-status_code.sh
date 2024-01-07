#!/usr/bin/bash
# a bash script to get the status code of the request to the geven URL
curl -w '%{response_code}' "$1" -so /dev/null
