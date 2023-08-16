#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for element in range(len(my_list)):
        if my_list[element] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[element])
    return new_list
