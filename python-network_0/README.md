## Learning Objectives
- What a URL is
- What HTTP is
- How to read a URL
- The scheme for a HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser (Application level)

## Requirements
Allowed editors: vi, vim, emacs
- A README.md file, at the root of the folder of the project, is mandatory
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your Bash scripts should be exactly 3 lines long (wc -l file should print 3)
- All your files should end with a new line
- All your files must be executable
- The first line of all your bash files should be exactly #!/bin/bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- All curl commands must have the option -s (silent mode)
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- The first line of all your Python files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.7.)
- All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
- All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
- All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Description Of Tasks
- [0-body_size.sh](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_0/0-body_size.sh) - Script to fetch a url and display size of body response in bytes
- [1-body.sh](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_0/1-body.sh) - Take a URL, send a GET request and display body of response if status code is 200
- [2-delete.sh](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_0/2-delete.sh) - Script to send DELETE request to the URL passed as first argument and display body of response
- [3-methods.sh](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_0/3-methods.sh) - Script to take URL and display HTTP methods that the server allows
- [4-header.sh](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_0/4-header.sh) - Script that takes URL as argument, sends GET request and displays body of the response. In addition, the named header variable must sent with the value 98
- [5-post_params.sh](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_0/5-post_params.sh) - Script that takes a URL, sends POST request and displays body of response. The POST request must be sent with email and subject params along with their corresponding given values
- [100-status_code.sh](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_0/100-status_code.sh) - Script to send a request to a URL passed as an argument and display the status code of the response
- [101-post_json.sh](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_0/101-post_json.sh) - Script to send a JSON POST request to URL passed as first argument and display body of response
- [102-catch_me.sh](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_0/102-catch_me.sh) - Script to make request to given URL that causes server to respond with the message 'You got me!' in body of response

