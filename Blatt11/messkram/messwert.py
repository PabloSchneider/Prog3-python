from nis import match
import re
from tkinter.tix import MAIN
from warnings import catch_warnings

from pip import main
class Messwert:
    
    def __init__(self, zeitpunkt, temperatur = None):
        _patternZeit = re.compile(r'[0-9]{4}(-[0-9]{2}){2} (([0-9]{2}:){2}[0-9]{2})[.]([0-9]){2,7}')
        _patternTemp = re.compile(r'[0-9]{2}.[0-9]{1,5}')
        
        try:
            if temperatur == None:
                matchZeit = _patternZeit.match(zeitpunkt[0].replace("\"",""))
                matchTemp = _patternTemp.match(zeitpunkt[1])
            else:
                matchZeit = _patternZeit.match(zeitpunkt.replace("\"",""))
                matchTemp = _patternTemp.match(temperatur)
            self._zeitpunkt = matchZeit.group()
            self._temeratur = matchTemp.group()
        except ValueError as ve:
            print("hallo", ve);

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

if __name__ == "__main__":
    
    mw = Messwert(["2018-07-30 00:00:01.410123","35.4375"])
    print(mw)