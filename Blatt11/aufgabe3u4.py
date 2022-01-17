#!/usr/bin/env python3

from aufgabe1 import Messwert
from typing import Iterable

class Messreihe:


    def __init__(self, data = None):
        self._reihe = list([Messwert(y.split(",")) for y in open('messwerte.csv')] if data == None else data)

    def __len__(self):
        return(len(self._reihe))

    def __iter__(self):
        self.pos= -1
        return self

    def __next__(self):
        self.pos += 1
        if self.pos >= len(self._reihe):
            raise StopIteration
        return self._reihe[self.pos]

    def __getitem__(self, subscript):
        return self._reihe[subscript]

    def __add__(self, new):
        assert(isinstance(new[0] ,str) and isinstance(new[1] ,float)), new 
        m = Messreihe(self._reihe.append(new))
        return m
    
    def add(self, neuwerte : Messwert):
        if isinstance(neuwerte, Iterable):
            for i in neuwerte:
                if i not in self._reihe:
                    assert(isinstance(i._zeitpunkt, str) and isinstance(i._temeratur, float)), i
                    self._reihe.append(i)
        else:
            if neuwerte not in self._reihe:
                assert(isinstance(neuwerte._zeitpunkt, str) and isinstance(neuwerte._temeratur, float)), neuwerte

                self._reihe.append(neuwerte)

    def addiert(self, messreihe1, messreihe2= None):
        messreihe1 = list(messreihe1)
        for x in messreihe1:
            
            if messreihe2 != None:
                messreihe2 = list(messreihe2)
                if x not in messreihe2:
                    messreihe2.append(x)
            else:
                if x not in self._reihe:
                    self._reihe.append(x)
        
        if messreihe2 != None:
            self._reihe = messreihe2

    def search(self, suche):
        if isinstance(suche, int):
            return self._reihe[suche]
        if isinstance(suche, str):
            return Messreihe([a for a in self._reihe if suche in a._zeitpunkt])
    
mr = Messreihe()

mr.add(Messwert("2019-05-12 13:30:01.922924",100.3))
for m in mr:
    print(m._zeitpunkt,"  ", m._temeratur)