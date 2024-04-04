## Learning Objectives
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

## Desription Of Tasks
- [0-hbtn_status.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/0-hbtn_status.py) - Script to fetch a url and display body of response
- [1-hbtn_header.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/1-hbtn_header.py) - Script to take URL, sends request and display value of X-Request-Id variable found in header of response
- [2-post_email.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/2-post_email.py) - Script that takes URL and email, sends POST request with email as param, and display body of response
- [3-error_code.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/3-error_code.py) - Script that takes URL, sends request and display body. Script should be able to handle HTTPError exeptions and in this case should print the error code
- [4-hbtn_status.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/4-hbtn_status.py) - Script that fetches url using requests package
- [5-hbtn_header.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/5-hbtn_header.py) - Script to take URL, send request and display value of variable X-Request-Id using the requests package
- [6-post_email.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/6-post_email.py) - Script to take URL and email, send POST request with eail as param, then display body of response using requests package
- [7-error_code.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-network_1/7-error_code.py) - 
