# Ein Element in einem Tuple an einer spezifischen Stelle löschen
prim = (2, 3, 5, 7, 11, 12, 13 )
print(prim)
n = 5
# Kopie mit Elementen von 0 bis n-1
v = prim[ : n]
# Kopie mit Elementen von n + 1 bis Ende
h = prim[n + 1: ]
prim = v +  h
print(prim)