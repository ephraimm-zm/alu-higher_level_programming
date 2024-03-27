#!/bin/bash
# Send a JSON POST to a URL
curl -s -H "Content-Type: application/json" -X POST -d '{"key": "value"}' "$1"
