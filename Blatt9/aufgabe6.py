#!/usr/bin/env python3

def permutationen(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in permutationen(elements[1:]):
            for i in range(len(elements)):                

                yield perm[:i] + [elements[0]] + perm[i:]
                print("i = ",i)
                print("1", perm[:i])
                print("2", [elements[0]])
                print("3", perm[i:])


for p in permutationen([1,2,3]):
    print(p)