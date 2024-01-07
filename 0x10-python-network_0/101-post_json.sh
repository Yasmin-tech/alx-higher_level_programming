#!/bin/bash
# a Bash script that sends a JSON POST request to a URL "first arg", json file "second arg"
curl -sX POST -d @"$2" "$1" --header "Content-Type:application/json"
