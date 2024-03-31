#!/usr/bin/python3
"""
Takes URL, sends request, display value of X-Request-Id
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        print(response.headers['X-Request-Id'])
    except:
        pass
