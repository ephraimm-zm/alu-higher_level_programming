#!/usr/bin/python3
"""
Fetch url and display status
"""
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    if url.startswith("https://"):
        url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
