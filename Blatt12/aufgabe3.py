from itertools import count
import re
import socket

bildpattern = re.compile(r'.*(([.]jpg)|([.]png)|([.]gif)).*')
timepattern = re.compile(r'(:[0-9]{2}){3}')
domainpattern = re.compile(r'[w]{3}\..*\.de')

counter = 0
times = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
domaincounter = {}
for line in open("/Users/pablo/prog3-python/access.log"):
    matchbild = bildpattern.match(line)
    if matchbild:
        counter += 1;
    machttime = timepattern.search(line)
    if machttime:
        time = machttime.group()
        time = time.split(':')
        times[int(time[1])] +=1
    machdomain = domainpattern.search(line)
    if machdomain:
        domain = machdomain.group()
        domain = domain.split('.')
        key = domain[-2] +'.'+ domain[-1]
        print(key)
        if key in domaincounter:
            domaincounter[key] = domaincounter[key] +1
        else:
            domaincounter[key] = 1
        print(domain)
    
print(socket.gethostbyaddr('195.72.105.32'))
print(counter)
print("[  0,   1,  2,  3,  4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23]")
print(times)
domaincounter = sorted(domaincounter.items(), key=lambda x: x[1], reverse=True)
for dom in domaincounter:
    print(dom[0], " ", dom[1])
