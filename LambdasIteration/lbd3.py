mein_tupel = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144)
meine_liste = []
lbd = lambda x: x % 2
meine_liste = filter(lbd,mein_tupel)
for x in meine_liste:
    print(x)