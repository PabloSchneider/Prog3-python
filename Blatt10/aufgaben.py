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
    
    
#--------------Aufgabe1--------------#
#messwerte1 = [Messwert(y.split(",")) for y in open('messwerte.csv')]
#messwerte2 = [Messwert(y.split(",")) for y in open('messwerte.csv')]
#sorted(messwerte)
#print(messwerte)
#print(set(messwerte))
#print(eval(repr(x)) == x)
#print(x < y)
mr1 = Messreihe([
Messwert("2013-07-15 16:03:08.260597",19.875),
Messwert("2013-07-15 16:15:01.997792",19.5625),
Messwert("2013-07-15 16:30:01.455079",20.3125),
Messwert("2013-07-15 17:00:01.201636",20.0625),
Messwert("2013-07-15 17:15:01.618921",20.625),
Messwert("2013-07-15 17:30:02.060205",19.75),
Messwert("2013-07-15 17:42:38.733501",20.1875)
])
mr2 = Messreihe([
Messwert("2013-07-15 18:30:01.251394",20.4375),
Messwert("2013-07-15 18:45:01.420677",20.375),
Messwert("2013-07-15 19:00:01.885987",19.5625),
Messwert("2013-07-15 19:15:01.231257",20.1875),
Messwert("2013-07-15 19:30:01.720501",20.1875),
Messwert("2013-07-15 19:45:02.073782",19.0625),
Messwert("2013-07-15 17:42:38.733501",20.1875)
])
mr = Messreihe()
print(len(mr1))
mr1.add(mr2)
print(len(mr1))
#--------------Aufgabe2--------------#
#mess1 = Messreihe()
#print(len(mess1))

#newMess = Messreihe(mess1[10:100])
#print(len(newMess))
#for n in newMess:
#    print(n)
#print(newMess)
#--------------Aufgabe3--------------#
'''
mess = Messreihe()
print("länge: ", len(mess))
print("min temp: ", min([x._temeratur for x in mess]))
print("max temp: ", max([x._temeratur for x in mess]))

print("Temperatur über 33 Grad:",[x._zeitpunkt for x in mess if float(x._temeratur) > 33])
print("Temperatur über 26 Grad 2017:",[x._zeitpunkt for x in mess.search("2017-") if float(x._temeratur) > 26])
print("Temperatur zuletzt bei 17 c", [x._zeitpunkt for x in mess if 18 < float(x._temeratur) > 16.9][-1])

m10 = [x for x in mess.search("2017-10")]
m11 = [y for y in mess.search("2017-11")]
m12 = [z for z in mess.search("2017-12")]
for m in m11:
    m10.append(m)
for n in m12:
    m10.append(n)
zahl = 0
for e in m10:
    zahl += float(e._temeratur)
zahl = zahl/len(m10)
print("Mittelwert der Temperaturen:", zahl)
'''