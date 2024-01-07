#!/bin/bash
# Send a DELETE request to a given URL and display the response body.
curl -Is "$1" | grep Allow | sed 's/Allow: //' 
