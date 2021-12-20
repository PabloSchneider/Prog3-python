#!/usr/bin/env python3
def restloseTeiler(z):
    teiler = []
    for i in range(z-1):
        if i > 1:
            if z % i == 0:
                teiler.append(i)
    return teiler
def isPrim()

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [123,12345,123456]
erg1 = [x for x in list1 if (x**3) % 2 == 0]
erg2 = [restloseTeiler(x) for x in list2]
erg3 = [x for x in range(10000,10100)]
print(erg1)
print(erg2)
