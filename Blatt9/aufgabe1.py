#!/usr/bin/env python3

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [123,12345,123456]
list3 = [x for x in range(10000,10100)]
#--------------------------------- Aufgabe 1 a--------------------------------------#

def restloseTeiler(z):
    teiler = []
    for i in range(z-1):
        if i > 1:
            if z % i == 0:
                teiler.append(i)
    return teiler
def isPrim(x):
    if x > 1:
        for i in range(2, int(x/2)+1):
            if (x%i) == 0:
                break
            else:
                return x

erg1 = [x**3 for x in list1 if (x**3) % 2 == 0]
erg2 = [restloseTeiler(x) for x in list2]
erg3 = [isPrim(x) for x in range(10000,10100)if isPrim(x) is not None]
print("---a---")
print(erg1)
print(erg2)
print(erg3)

#--------------------------------- Aufgabe 1 b--------------------------------------#
print("---b---")
berg1 = list(map(lambda x: x**3 ,(filter(lambda x: (x**3)%2 == 0, list1))))
berg2 = list(map(restloseTeiler, list2))
berg3 = list(filter(isPrim, list3))
print(berg1)
print(berg2)
print(berg3)