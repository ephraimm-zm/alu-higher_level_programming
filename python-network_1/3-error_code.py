#!/usr/bin/python3
"""
Take a URL, send request, display body decoded in utf-8
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
