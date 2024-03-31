#!/usr/bin/python3
"""
Take URL and email, send POST, display body of response
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, email)
    print(response.text)
