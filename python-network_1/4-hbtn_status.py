#!/usr/bin/python3
"""
Fetch url and display status
"""
import requests

if __name__ == "__main__":
    response = requests.get("https://alu-intranet.hbtn.io/status")
    print("Body response:")
    print("\t - type:", type(response.text))
    print("\t - content:", response.text)
