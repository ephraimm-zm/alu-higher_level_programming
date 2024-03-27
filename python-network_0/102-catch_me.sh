#!/bin/bash
# Send a POST request with specific data to target URL
curl -s -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" "0.0.0.0:5000/catch_me" --output /dev/null -w "You got me!"
