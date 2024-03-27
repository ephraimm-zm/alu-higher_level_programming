#!/bin/bash
# Send a JSON POST to a URL
curl -s -H "Content-Type: application/json" -X POST -d "@2" "$1"
