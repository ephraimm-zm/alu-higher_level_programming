#!/bin/bash
# Send GET request with header var and value and display body
curl -sH "X-School-User-Id: 98" "$1"
