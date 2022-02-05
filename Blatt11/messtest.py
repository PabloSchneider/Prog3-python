
from random import gauss
from messkram.messreihe import Messreihe


def makeMessreihe(jahr, monat, tag, anzahl):
    mr = Messreihe()
    if monat < 10:
        datestr = str(jahr)+"-0"+str(monat)+"-"+str(tag)
    else:
        datestr = str(jahr)+"-"+str(monat)+"-"+str(tag)

    datestr = datestr.strip(" ")
    newMessreihe = []
    
    for m in mr:
        date = str(m._zeitpunkt)
        date = date.split(" ")[0]
        date = date.strip(" ")
        if date >= datestr and len(newMessreihe) <= anzahl:
            newMessreihe.append(m)
    
    newMr = Messreihe(newMessreihe)
    
    return newMr

def messreihe2Text(mr):
    for m in mr:
        yield '"'+m._zeitpunkt+'"'+","+str(m._temeratur)

if __name__ == '__main__':
    mp = makeMessreihe(2018,7,30,200)
    for v in mp:
        print(v._zeitpunkt)
    print("gauss",gauss(17,3))
    f = open("newMess.csv","w")
    f.writelines(messreihe2Text(mp))
    f.close
    lst = messreihe2Text(mp)
    for m in lst:
        print(m)
