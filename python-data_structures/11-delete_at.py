#!/usr/bin/python3
def delete_element_at_index(my_list, index):
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = my_list[:idx] + my_list[idx+1:]
    return new_list
