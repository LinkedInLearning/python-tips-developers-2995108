import sys
tupABC = ('a', 'b', 'c')

print("Referenz-Counter eines Tupel mit 3 Elementen: %s" % sys.getrefcount(tupABC))
print("Referenz-Counter Element 1 nach Position in der Liste: %s" % sys.getrefcount(tupABC[0]))
print("Referenz-Counter Element 1 nach Inhalt: %s" % sys.getrefcount('a'))
print("Referenz-Counter Element 2 nach Position in der Liste: %s" % sys.getrefcount(tupABC[1]))
print("Referenz-Counter Element 2 nach Inhalt: %s" % sys.getrefcount('b'))
print("Referenz-Counter Element 3 nach Position in der Liste: %s" % sys.getrefcount(tupABC[2]))
print("Referenz-Counter Element 3 nach Inhalt: %s" % sys.getrefcount('c'))
 
print("\n", "*" * 40, "Tupel wird gelöscht", "*" * 40,"\n")  
del(tupABC)
print("Referenz-Counter Element 1 nach Inhalt: %s" % sys.getrefcount('a'))
print("Referenz-Counter Element 2 nach Inhalt: %s" % sys.getrefcount('b'))
print("Referenz-Counter Element 3 nach Inhalt: %s" % sys.getrefcount('c'))