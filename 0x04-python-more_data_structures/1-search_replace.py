#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return [replace if search == elem else elem for elem in my_list]
