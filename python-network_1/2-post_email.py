#!/usr/bin/python3
"""
Take URL and email, send POST, display body decoded in utf-8
"""
import urllib.request
import sys

if __name__ == "__main__":
"""
documentaion bloody
"""
    url = sys.argv[1]
    email = sys.argv[2]

    req = urllib.request.Request(url, data=email.encode('utf-8'))

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8')
