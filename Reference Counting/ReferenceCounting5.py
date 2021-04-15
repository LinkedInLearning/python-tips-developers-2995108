import sys
liABC = ['a', 'b', 'c']

print("Referenz-Counter einer Liste mit 3 Elementen: %s" % sys.getrefcount(liABC))
print("Referenz-Counter Element 1 nach Position in der Liste: %s" % sys.getrefcount(liABC[0]))
print("Referenz-Counter Element 1 nach Inhalt: %s" % sys.getrefcount('a'))
print("Referenz-Counter Element 2 nach Position in der Liste: %s" % sys.getrefcount(liABC[1]))
print("Referenz-Counter Element 2 nach Inhalt: %s" % sys.getrefcount('b'))
print("Referenz-Counter Element 3 nach Position in der Liste: %s" % sys.getrefcount(liABC[2]))
print("Referenz-Counter Element 3 nach Inhalt: %s" % sys.getrefcount('c'))
 
print("\n", "*" * 40, "Liste wird gelöscht", "*" * 40,"\n")  
del(liABC)
print("Referenz-Counter Element 1 nach Inhalt: %s" % sys.getrefcount('a'))
print("Referenz-Counter Element 2 nach Inhalt: %s" % sys.getrefcount('b'))
print("Referenz-Counter Element 3 nach Inhalt: %s" % sys.getrefcount('c'))