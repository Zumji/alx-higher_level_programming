#!/usr/bin/python
def safe_print_list_integers(my_list=[], x=0):
    ret = 0
    for i in range (0, x):
    try: 
        print("{:d}".format(my_list[i]), end="")
    except ValueError:
        continue 
    print("")
    return (ret)

