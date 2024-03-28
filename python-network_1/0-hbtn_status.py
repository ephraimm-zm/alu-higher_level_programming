#!/usr/bin/python3
"""
This script fetches the status from a specified URL using the urllib package
and displays information about the response body.
"""

import urllib.request

# URL to fetch status from
url = "https://alu-intranet.hbtn.io/status"

if __name__ == "__main__":

	# Fetch the URL and process the response
	with urllib.request.urlopen(url) as response:
    	# Read the body of the response
    	body = response.read()

    	# Display information about the response body
    	print("Body response:")
    	print("\t- type:", type(body))
    	print("\t- content:", body)
    	print("\t- utf8 content:", body.decode('utf-8'))
