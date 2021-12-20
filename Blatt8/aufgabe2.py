#!/usr/bin/env python3


def ggTr(x,y):
    if x == y:
        return x 
    else:
        if x > y:
           return ggTr(x-y, y)
        else:
           return ggTr(y,x)

def ggT(x,y):
    while x % y != 0:
        if x > y:
            x, y = y, x%y
        else:
            x,y = y,x;
    return y

def ggT1(x,y,*z):

    a = ggT(x,y)
    for zahl in z:
        a = ggT(a,zahl)
    return a


print(ggT1(8,4,6,10,12))
print(ggT1(10,80,20,75))
print(ggT1(17,4))
print(ggT1(10,20,100,300,20,4000))
'''
for line in open("ggtbeispiele.txt"):
    #print(line)
    elements = line.split()

    print("TEST GGT:", ggT(int(elements[0]),int(elements[1])), " ==? ", elements[2])

x = ggTr(20,30)
y = ggT(20,30)
print("Die Zahl ist",x, "oder", y)
'''

