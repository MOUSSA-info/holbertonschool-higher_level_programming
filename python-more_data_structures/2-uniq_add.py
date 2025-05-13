#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set()
    for num in my_list:
        unique.add(num)
    total = 0
    for num in unique:
        total += num
    return total
