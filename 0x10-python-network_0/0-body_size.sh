#!/bin/bash
# This script takes a URL as input, sends a request.
curl -s "$1" | wc -c
