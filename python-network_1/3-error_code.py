#!/usr/bin/python3
"""
Take a URL, send request, display body decoded in utf-8
Usage: ./3-error_code <URL>
"""


import sys
import urllib.request, error
if __name__ == "__main__":

    try:
        with request.urlopen(sys.argv[1]) as resq:
            print(resq.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
