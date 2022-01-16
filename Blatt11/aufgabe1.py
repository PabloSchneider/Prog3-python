#!/usr/bin/env python3

from typing import Iterable


class Messwert:

    def __init__(self, zeitpunkt, temperatur = None):
        
        if temperatur == None:
            self._zeitpunkt = zeitpunkt[0].replace("\"","")
            self._temeratur = zeitpunkt[1]       
        else:
            self._zeitpunkt = zeitpunkt.replace("\"","")
            self._temeratur = temperatur

    def __repr__(self):
        return f'Messwert("{self._zeitpunkt}",{self._temeratur})'


    def __eq__(self, x):
        return True if (self._zeitpunkt == x._zeitpunkt and self._temeratur == x._temeratur) else False

    def __lt__(self, x):
        if x._zeitpunkt < self._zeitpunkt:
            return True
        elif x._zeitpunkt == self._zeitpunkt:
            if x._temeratur < self._temeratur:
                return True     
        return False
    def __hash__(self):
        return hash((self._zeitpunkt, self._temeratur))

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

    def add(self, neuwerte):
        if isinstance(neuwerte, Iterable):
            for i in neuwerte:
                if i not in self._reihe:
                    self._reihe.append(i)
        else:
            if neuwerte not in self._reihe:
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
    
class MessreiheEigenIter:
    def __init__(self, mr):
        self._mr = mr
        self.pos = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.pos += 1
        if self.pos >= len(self._mr):
            raise StopIteration
        return self._mr[self.pos]

class MessreiheGenIter:
    def __init__(self, mr):
        self._mr = mr

    def erzugeIterator(self):
        for w in self.mr:
            yield w

    def __iter__(self):
        return self.erzugeIterator()


def main():
    
    mw = Messreihe()
    it1, it2 = iter(mw), iter(mw)
    print("___________________________________________")
    for i in range(10):
        m1, m2 = next(it1), next(it2)
        print(m1, m2, "Problem" if m1 != m2 else "OK")
    print("___________________________________________")

    iter1, iter2 = MessreiheEigenIter(mw), MessreiheEigenIter(mw)

    print("___________________________________________")
    for i in range(10):
        m1, m2 = next(iter1), next(iter2)
        print(m1, m2, "Problem" if m1 != m2 else "OK")
    print("___________________________________________")

    iter1, iter2 = MessreiheGenIter(mw), MessreiheGenIter(mw)

    print("___________________________________________")
    for i in range(10):
        m1, m2 = next(iter1), next(iter2)
        print(m1, m2, "Problem" if m1 != m2 else "OK")
    print("___________________________________________")


if __name__ == '__main__':
    main()