#!/bin/bash
# Script to display size of the body of the response
curl -sI "$url" | grep -i '^Content-Length:' | awk '{print $2}' | tr -d '\r'
