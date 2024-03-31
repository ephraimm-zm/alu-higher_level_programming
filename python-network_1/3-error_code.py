#!/usr/bin/python3
"""
Take a URL, send request, display body decoded in utf-8
Usage: ./3-error_code <URL>
"""


import sys
import urllib.request
import urllib.error
if __name__ == "__main__":

    try:
        req = urllib.request.Request(sys.argv[1])
        with request.urlopen(sys.argv[1]) as resq:
            print(resq.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
