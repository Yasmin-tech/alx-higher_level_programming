#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl --write-out '%{size_request}' -so /dev/null "$1"
