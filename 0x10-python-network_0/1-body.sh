#!/bin/bash
# sends GET request to the URL and displays the body of the response

curl -sL "$1"
#if [ "$(curl -sLI "$1" -X GET | grep "200 OK" | cut -d' ' -f2)" = '200' ]; then curl -sL "$1"; fi
