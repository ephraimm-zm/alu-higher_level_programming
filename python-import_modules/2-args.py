#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    arg_count = len(argv)

    if arg_count == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    elif arg_count > 2:
        print("{} arguments:".format(arg_count - 1))  # Subtract 1 to exclude the script name
        for i, arg in enumerate(argv[1:], start=1):  # Start from index 1 to exclude the script name
            print("{}: {}".format(i, arg))
    else:
        print("0 arguments")

