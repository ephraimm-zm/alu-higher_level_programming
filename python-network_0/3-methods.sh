#!/bin/bash
# Take URL and display HTTP methods allowed
curl -s -i "$1" | grep -i "Allow:" | cut -d' ' -f2-
