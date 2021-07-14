z = 777
tmp = list(map(int,str(z)))
print(tmp, type(tmp))
qs1 = sum([int(i) for i in tmp])
print(qs1)
qs2 = 0
for i in tmp:
    qs2+=i
print(qs2)
qs3 = 0
i = 0
t = 0
a = z
while i < len(str(z)):
    t += a % 10
    a = int(a / 10)
    i+=1
qs3 = t
print(qs3)