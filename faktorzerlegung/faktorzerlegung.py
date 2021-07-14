z = 12345678
fz1, fz2, fz3, fz4 = [],[],[],[]

for i in str(z):
    fz1.append(i)
print(fz1, type(fz1))

i = 0
while i < len(str(z)):
    fz2.append(str(z)[i])
    i += 1
print(fz2, type(fz2))

for i in str(z):
    fz3.append(int(i))
print(fz3, type(fz3))

fz4 = list(map(int,str(z)))
print(fz4, type(fz4))