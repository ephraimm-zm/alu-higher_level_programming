#!/bin/bash
# Send POST request and display body
curl -s -X POST -d "email=tes@gmail.com&subject=I will always be here for PLD" "$1"
