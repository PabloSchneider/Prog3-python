#!/usr/bin/env python3


def dreh(lst: list):
    return [] if not lst else dreh(lst[1:]) + [lst[0]]

lst = [1,2,3,4,5,6,7,8]
print(dreh(lst))

