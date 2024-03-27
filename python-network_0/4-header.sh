#!/bin/bash
# Send GET request with header var and value and display body
curl -s -H "X-HolbertonSchool-User-Id" -X GET "$1"
