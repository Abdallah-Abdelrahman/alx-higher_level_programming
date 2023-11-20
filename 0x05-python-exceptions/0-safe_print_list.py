#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0

    try:
        while i < x:
            print(my_list[i], end='')
            i += 1;
        print()
    except IndexError:
        print()
    finally:
        return i

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))


