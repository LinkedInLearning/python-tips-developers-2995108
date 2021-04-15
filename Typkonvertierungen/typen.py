werte = (1, 3.1, True, "1", 1+1j, (), [], set(), {}, frozenset(), b'abc', range(1,100))
index=0
for x in werte:
    print(index, ": Wert", x, ", Typ: ", type(x))
    index += 1

print("Wert", werte[3], ", Typ: ", type( werte[3]))
cast = int(werte[3])
print("Wert", cast, ", Typ: ", type( cast))

print("Wert", werte[10],", Typ: ", type(werte[10]))
cast =  str(werte[10])
print("Wert", cast,", Typ: ", type(cast))

print("Wert", werte[9],", Typ: ", type(werte[9]))
cast =  set(werte[9])
print("Wert", cast,", Typ: ", type(cast))

print("Wert", werte[6],", Typ: ", type(werte[6]))
cast =  tuple(werte[6])
print("Wert", cast,", Typ: ", type(cast))

print("Wert", werte[11],", Typ: ", type(werte[11]))
cast =  list(werte[11])
print("Wert", cast,", Typ: ", type(cast))