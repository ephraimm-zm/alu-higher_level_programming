#!/bin/bash
# Script t osend request and display only status code
curl -s -o /dev/null -w "%{http_code}" "$1"
