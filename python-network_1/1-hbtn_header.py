#!/usr/bin/python3
"""
This module sends a request to a specified URL and displays the value of X-Request-Id header in the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.getheader("X-Request-Id"))
