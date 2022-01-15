#!/usr/bin/env python3

#wohnorte aller Männer
print(sorted([x.split(";")[4].replace("\n","") for x in open("bonz.txt").readlines() if x.split(";")[0] == "Herr"]))

#summe der Gehälter aller Frauen
print(sum([int(x.split(";")[3]) for x in open("bonz.txt").readlines() if x.split(";")[0] == "Frau"]))

#wohnort der person, die am meisten verdient und mit j anfängt

print([ x.split(";")[4].replace("\n","") for x in open("bonz.txt").readlines() if int(x.split(";")[3]) == max([int(x.split(";")[3].replace("\n","")) for x in open("bonz.txt").readlines() if x.split(";")[2][0] == "J"])])

#schaming von personen, die zuviel verdienen!

print([str(x.split(";")[0])+" "+str(x.split(";")[1])+" bekommt mehr, als "+ ("er" if str(x.split(";")[0]) == "Herr" else "sie") +" verdient" for x in open("bonz.txt").readlines() if int(x.split(";")[3]) >= 100000])