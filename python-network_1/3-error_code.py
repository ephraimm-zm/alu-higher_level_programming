#!/usr/bin/python3
"""
Take a URL, send request, display body decoded in utf-8
Usage: ./3-error_code <URL>
"""


if __name__ == "__main__":
    import sys
    import urllib.request, error
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
