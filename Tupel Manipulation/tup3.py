# Ein Element in einem Tuple an einer spezifischen Stelle hinzufügen
prim = (2, 3, 5, 7, 13 )
print(prim)
n = 4
# Kopie mit Elementen von 0 bis n-1
v = prim[ : n]
# Kopie mit Elementen von n bis Ende
h = prim[n : ]
prim = v + (11,) + h
print(prim)