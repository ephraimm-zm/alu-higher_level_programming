#!/usr/bin/python3
"""
Takes letter, sends POST with letter as param
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': q})

    try:
        data = response.json()
        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data.get('id'), data.get('name')))
    except ValueError:
        print("Not a valid JSON")
