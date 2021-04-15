import copy as cp
a = [2,3,5,True,7,"Text",11, (13,17,19)] # Listen
print("Typ von a: %s" % type (a))
print("Inhalt von a: %s" % a)
for i in a:
    print(i)
print("*" * 50)
print(a[2])
b = a # Zuweisung von a zu einer neuen Variablen b
print("a wird verändert.")
a[2]=55
a.append(77)
print("Inhalt von a: %s" % a)
print("Inhalt von b: %s" % b)
print("*" * 50)
print("a wird Originalzustand gesetzt.")
a = [2,3,5,True,7,"Text",11, (13,17,19)] 
print("Inhalt von a: %s" % a)
b = cp.copy(a)  # Clonen
print("Inhalt von b: %s" % b)
print("a wird verändert.")
a[2]=55
a.append(77)
print("Inhalt von a: %s" % a)
print("Inhalt von b: %s" % b)
print("*" * 50)