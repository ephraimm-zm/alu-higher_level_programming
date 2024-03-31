#!/usr/bin/python3
"""
Take GitHub user and repo name, list 10 commits in desc order
"""

import requests
import sys

if __name__ == "__main__":

    repo = sys.argv[1]
    repo = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)


