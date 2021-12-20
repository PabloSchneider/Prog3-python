#!/usr/bin/env python3

def auskunft(linie, start, ziel):
    fahrplan = []
    stationen = []
    fahrdauer = 0
    newziel = ziel
    for fahrt in open("fahrzeiten.txt"):
    
        fahrt = fahrt.split(';')
        fahrt[3] = int(fahrt[3].replace("\n", ""))
        fahrplan.append(fahrt)
    filteredfahrten = filter(linie, fahrplan)
    while start != ziel:
        for fahrt in filteredfahrten:
            if fahrt[1] == start:
                if start != ziel:
                    print(start)
                    stationen.append(fahrt[1])
                    start = fahrt[2]
                    fahrdauer = fahrdauer + fahrt[3]
    stationen.append(ziel)
    return (fahrdauer, stationen)


def filter(linie, fahrplan):
    filteredfahrten = []
    for line in fahrplan:
        if line[0] == linie:
            filteredfahrten.append(line)
    return filteredfahrten

linie = "S9"
start = "Kelsterbach"
ziel = "Niederrad"
print(auskunft("Bus6", "Nordfriedhof", "Nordfriedhof"))
minuten,weg = auskunft("S9", "Kelsterbach", "Niederrad")
print(minuten,"Minuten so:",weg)


