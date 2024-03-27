#!/bin/bash
# Script to display size of the body of the response
curl -s -L "$1" | tee response.txt | wc -c
