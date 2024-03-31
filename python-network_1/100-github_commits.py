#!/usr/bin/python3
"""
Take GitHub user and repo name, list 10 commits in desc order
"""

import requests
import sys

if __name__ == "__main__":

    repo = sys.argv[1]
    user = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)

    response = requests.get(url)
    if response.status_code == 200:
        commits_data = response.json()
        for commit in commits_data[:10]:
                print("{}: {}".format(
                    commit['sha'],
                    commit['commit']['author']['name']
                ))
    else:
        pass
