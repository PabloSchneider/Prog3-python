i = 0
liste = []
for i in range(101):
    liste.append(i)

print("ersten 10 elemente",liste[:10])
print("letzten 10 elemente",liste[-10:])
print("jede 10te zahl",liste[::10])
print("mittlere zahl",liste[(len(liste)//2):(len(liste)//2+1)])
print("jede 3te nicht ersten 4 nicht letzen 5", liste[4*3:-5*3:3])



