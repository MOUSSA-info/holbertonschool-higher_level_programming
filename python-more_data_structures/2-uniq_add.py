#!/usr/bin/python
def uniq_add(my_list=[]):
    unique = []
    for num in my_list:
        if num not in unique:
            unique.append(num)
    total = 0
    for num in unique:
        total += num
    return total
