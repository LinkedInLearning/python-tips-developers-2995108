# Ein Element in einem Tuple an einer spezifischen Stelle modifizieren oder ersetzen
prim = (2, 3, 5, 7, 10, 13 )
print(prim)
n = 4
# Kopie mit Elementen von 0 bis n-1
v = prim[ : n]
# Kopie mit Elementen von n + 1 bis Ende
h = prim[n + 1: ]
prim = v + (11,) + h
print(prim)