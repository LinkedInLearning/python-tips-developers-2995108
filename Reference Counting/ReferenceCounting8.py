import sys
class Tier():
    def __init__(self):
        self.alter = 5
x = Tier()
print("Referenz-Counter Objekt 1: %s" % sys.getrefcount(x))

y = Tier()
print("Referenz-Counter Objekt 2: %s" % sys.getrefcount(y))
print("\n", "*" * 40, "Referenz-Counter auf x wird y zugewiesen", "*" * 40,"\n") 


z = x
print("Referenz-Counter Objekt 1: %s" % sys.getrefcount(x))
print("Referenz-Counter Objekt 2: %s" % sys.getrefcount(y))
print("Referenz-Counter Objekt 3: %s" % sys.getrefcount(z))
print("\n", "*" * 40, "x wird gelöscht", "*" * 40,"\n") 
del(x)
print("Referenz-Counter Objekt 2: %s" % sys.getrefcount(y))
print("Referenz-Counter Objekt 3: %s" % sys.getrefcount(z))

print(sys.getrefcount(z))