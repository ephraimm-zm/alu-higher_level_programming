#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = {}
    total = 0

    for number in my_list:
        if number not in unique:
            unique[number] = True
            total += number
    
    return total
