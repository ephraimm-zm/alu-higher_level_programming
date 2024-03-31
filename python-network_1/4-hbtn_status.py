#!/usr/bin/python3
"""
Fetch url and display status
"""
import requests

response = requests.get("https://alu-intranet.hbtn.io/status")

print("Body response:")
print("\t - type:", type(response)
print("\t - content:", response.content)
