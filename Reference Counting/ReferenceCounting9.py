import sys
import copy
class Tier():
    def __init__(self):
        self.alter = 5
x = Tier()
print("Referenz-Counter Objekt 1: %s" % sys.getrefcount(x))
print("\n", "*" * 40, "x wird kopiert unt y zugewiesen", "*" * 40,"\n") 

y = copy.copy(x)
print("Referenz-Counter Objekt 1: %s" % sys.getrefcount(x))
print("Referenz-Counter Objekt 2: %s" % sys.getrefcount(y))
print("\n", "*" * 40, "x wird gelöscht", "*" * 40,"\n") 
del(x)
print("Referenz-Counter Objekt 2: %s" % sys.getrefcount(y))
