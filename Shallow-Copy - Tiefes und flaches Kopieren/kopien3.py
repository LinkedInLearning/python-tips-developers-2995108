import copy as cp
a = [2,3,5,True,7,"Text",11, [13,17,19]] # Listen
print("Typ von a: %s" % type (a))
print("Inhalt von a: %s" % a)
b = cp.copy(a)
c = cp.deepcopy(a)
print("Inhalt von b: %s" % b)
print("Inhalt von c: %s" % c)
print("*" * 50)
print("a wird geändert.")
a[7][1] = 93
print("Inhalt von a: %s" % a)
print("Inhalt von b: %s" % b)
print("Inhalt von c: %s" % c)
