#!/usr/bin/python3
"""
Fetch url and display status
"""
import requests

if __name__ == "__main__":
    response = requests.get("https://alu-intranet.hbtn.io/status")
