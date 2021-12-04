#!/usr/bin/env python3


def dreh(lst:list):
    
    l = len(lst)
    if l > 1:
        first = lst.pop(0)
        lst = dreh(lst)
        lst.append(first)
    return lst

lst = [1,2,3,4,5,6,7,8]
print(dreh(lst))