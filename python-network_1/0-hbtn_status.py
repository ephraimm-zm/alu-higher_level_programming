#!/usr/bin/python3
"""
Fetches https://alu-intranet.hbtn.io/status
"""
import urllib.request


url = "https://alu-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
	body = response.read()
	print("Body resopnse:")
	print("\t- type:", type(body))
	print("\t- content:", body)
	print("\t- utf8 content:", body.decode('utf-8))
