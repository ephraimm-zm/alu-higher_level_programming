#!/bin/bash
# Send GET request with header var and value and display body
curl -s -H "X-School-User-Id" "$1"
