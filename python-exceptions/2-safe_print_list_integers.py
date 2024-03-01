#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for item in my_list[:x]:
        try:
            if isinstance(item, int):
                print("{:d}".format(item), end="")
                count += 1
        except Exception:
            pass
    return count
