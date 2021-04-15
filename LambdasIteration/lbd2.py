mein_tupel = (2, 3, 4, 5)
meine_liste = [3,6,9,11,12,17,20]
erg_liste1 = []
erg_liste2 = []
erg_liste3 = []
lbd1 = lambda x: x * 2
lbd2 = lambda x: x % 2
lbd3 = lambda x,y: x + y
erg_liste1 = map(lbd1,mein_tupel)
print(list(erg_liste1))
erg_liste2 = map(lbd2,meine_liste)
for x in erg_liste2:
    print(x)
erg_liste3 = map(lbd3,mein_tupel,meine_liste)
print(list(erg_liste3))
