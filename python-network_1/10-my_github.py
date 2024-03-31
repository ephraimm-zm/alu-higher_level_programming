#!/usr/bin/python3
"""
Take Github credentials, use GitHub API, display id
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))
    user_data = response.json()
    if response.status_code == 200:
        print(user_data['id'])
    else:
        print('None')
