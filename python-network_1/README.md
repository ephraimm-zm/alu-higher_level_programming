i# Learning Objectives
- How to fetch internet resources ith the Python package urllib
- How to decode urllib body response
- How to use the Python package requests #requestsiswaysimplerthanurllib
- How to make HTTP *GET* request
- How to make HTTP *POST/PUT*/etc request
- How to fetch JSON resources
- How to manipulate data from an external service

## Requirements
- Allowed editors: vi, vim, emacs.
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- Your code should not be executed when imported (by using if __name__ == "__main__":)

cription Of Tasks
- [0-hbtn_status.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/0-hbtn_status.py) - Fetch a url and display body of response using urllib package
- [1-hbtn_header.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/1-hbtn_header.py) - Send a request to a URL and display value of X-Request-Id using urllib package
- [2-post_email.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/2-post_email.py) - Using the urllib package, send POST request to URL passed as first argument with the email passed as second argument as a param. Display the body of the response decoded in utf-8
- [3-error_code.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/3-error_code.py) - Send a request to the URL passed as the first argument and display body of response. If HTTPError, print error code
- [4-hbtn_status.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/4-hbtn_status.py) - Fetch a url using the requests package
- [5-hbtn_header.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/5-hbtn_header.py) - Using the requests package, take URL, send a request, display value of X-Request-Id
- [6-post_email.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/6-post_email.py) - Take URL and email, send POST request with email as param and display body of response
- [7-error_code.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/7-error_code.py) - Take URL, send request and display body of response. If HTTP status code greater than 400, print the error code
- [8-json_api.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/8-json_api.py) - Take letter in argv[1], send POST request to url with letter as param, display 'id' and 'name' from body. If the body response is not valid JSON or the JSON is empty, display error message
- [10-my_github.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/10-my_github.py) - Script to take GitHub username and password, then send request to GitHub API and display 'id' fro response
- [100-github_commits.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/100-github_commits.py) - Script to take GitHub repository name and owner name, then sends request to GitHub API and then display last 10 commits from owner in desc order
