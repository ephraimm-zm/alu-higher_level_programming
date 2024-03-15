## Learning Objectives
- Why python programming is awesome
- What is an object
- What is the difference between a class and an object or instance
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7 and above)
- All your files must be executable
- The length of your files will be tested using wc

### .txt Answer Files
- Only one line
- No shebang
- All your files should end with a new line

## Description Of Files
- [0-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/0-answer.txt) - Contains the function used to print a type of object
- [1-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/1-answer.txt) - Contains the function to get the memory address in the CPython implementation
- [2-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/2-answer.txt) - Response to a question if two variables point to the same object
- [3-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/3-answer.txt) - Response to question if two variables point to the same object
- [4-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/4-answer.txt) - Response to a question if two variables point to the same object
- [5-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/5-answer.txt) - Response to a question if two variables point to the same object
- [6-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/6-answer.txt) - Response to a question about whether two variables equate to the same thing
- [7-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/7-answer.txt) - Response to a question about whether two variables refer to the same object in memory
- [8-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/8-answer.txt) - Response to a question about whether two variables equate to the same thing
- [9-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/9-answer.txt) - Response to a question about whether two variables refer to the same object in memory
- [10-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/10-answer.txt) - Response to a question about whether two variables equate to the same thing
- [11-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/11-answer.txt) - Response to a question about whether two lists refer to the same object in memory
- [12-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/12-answer.txt) - Response to a question about whether two lists equate to the same thing
- [13-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/13-answer.txt) - Response to a question about whether two lists refer to the same object in memory
- [14-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/14-answer.txt) - Response to a question about what would happen to a list after apending an element to another list that refers to the same object in memory of the first list
- [15-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/15-answer.txt) - Response to a question about what would happen to a list that pointed to the same object in memory when a new list is created and an element is appended to the new list.
- [16-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/16-answer.txt) - Response to what would happen if you tried to mutate an immutable int using an increment function
- [17-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/17-answer.txt) - Response to what would happen if you tried to mutate a list through a function by appending an element to the end
- [18-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/18-answer.txt) - Question to see what would happen if you mutate the local scope of a list inside a function and whether the original list outside the function will also be mutated
- [19-copy_list.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/19-copy_list.py) - Function that returns a copy of a list
- [20-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/20-answer.txt) - Response to whether an object is a tuple or not
- [21-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/21-answer.txt) - Response to whether an object is a tuple or not
- [22-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/22-answer.txt) - Response to whether an object is a tuple or not
- [23-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/23-answer.txt) - Response to whether an object is a tuple or not
- [24-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/24-answer.txt) - Response to whether two ints refer to the same object in memory
- [25-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/25-answer.txt) - Response to whether two tuples refer to the same object in memory
- [26-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/26-answer.txt) - Response to whether two empty tuples refer to the object
- [27-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/27-answer.txt) - Response to whether a list will still be the same object in memory after mutating it
- [28-answer.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/28-answer.txt) - Response to whether a list modified in place would still refer to the same list object in memory
- [100-magic_string.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/100-magic_string.py) - A function that returns Holberton n times
- [101-locked_class.py](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/101-locked_class.py) - A class that only accepts the creation of new instance attributes named first_name
- [103-line1.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/103-line1.txt) - A response to how many int objects are created after the execution of the first line of the given script
- [103-line2.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/103-line2.txt) - A response to how many int objects are created after the execution of the second line of the given script
- [104-line1.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/104-line1.txt) - Response to how many int objects are created after the execution of the first line of the given script
- [104-line2.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/104-line2.txt) - Response to how many int objects are created after the excecution of the second line of the given script
- [104-line3.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/104-line3.txt) - Response to if the int object pointed by a variable is deleted after the execution of the del function
- [104-line4.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/104-line4.txt) - Response to if the int object pointed by a variable is deleted after the excecution of the del function
- [104-line5.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/104-line5.txt) - Response to how many int objects are created after the execution of the last line of the given script
- [105-line1.txt](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/python-everything_is_object/105-line1.txt) - Response to how many int objects are created and are still in memory before the execution of the second line of a given script
