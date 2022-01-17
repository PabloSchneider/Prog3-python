#!/usr/bin/env python3
from aufgabe1 import Messwert
from aufgabe1 import Messreihe

def enum(iterable):
    index = -1
    for ele in iterable:
        index += 1
        yield (index, ele)

def main():
    mr = Messreihe()
    for nr, messwert in enum(mr):
        print(nr," --> ", messwert)

if __name__== '__main__':
    main()

