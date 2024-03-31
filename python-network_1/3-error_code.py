#!/usr/bin/python3
"""
Take a URL, send request, display body decoded in utf-8
Usage: ./3-error_code <URL>
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
