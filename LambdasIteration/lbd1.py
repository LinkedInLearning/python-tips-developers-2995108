mein_tupel = (2, 3, 4, 5)
meine_liste = [2, 3, 4, 5, 7, 9, 12]
lbd1 = lambda x: x * 2
lbd2 = lambda x: x % 2
for item in mein_tupel:
    print(lbd1(item),lbd2(item))
for item in meine_liste:
    print(lbd1(item),lbd2(item),(lambda x: x * x)(item))    

