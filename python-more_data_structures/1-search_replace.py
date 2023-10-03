#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None and search is not None and replace is not None:
        new_list = my_list.copy()
        for i in range(len(new_list) - 1):
            if new_list[i] == search:
                new_list[i] = replace
        return new_list
