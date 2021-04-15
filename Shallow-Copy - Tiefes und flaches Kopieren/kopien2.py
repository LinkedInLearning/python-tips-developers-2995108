import copy as cp

a = [2,3,7,5,1]
print("Inhalt von a: %s" % a)
b = cp.copy(a)  # Clone
c = a.copy()
print("Inhalt von b: %s" % b)
print("Inhalt von c: %s" % c)
print("*" * 50)
print("a wird verändert.")
a.sort()
#a.reverse()
print("Inhalt von a: %s" % a)
print("Inhalt von b: %s" % b)
print("Inhalt von c: %s" % c)
print("*" * 50)
print("a wird verändert.")
#a.sort()
a.reverse()
print("Inhalt von a: %s" % a)
print("Inhalt von b: %s" % b)
print("Inhalt von c: %s" % c)
