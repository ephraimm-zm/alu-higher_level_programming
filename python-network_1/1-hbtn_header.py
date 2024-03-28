#!/usr/bin/python3
"""
Take URL, send req to URL and display value of X-Request-Id
"""
import urllib.request
import sys

url = sys.argv[1]

if __name__ == "__main__":
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       print(response.getheader("X-Request-Id")
