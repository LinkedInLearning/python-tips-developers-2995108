a = 1
b = 2
print(a, b)
temp = a
a = b
b = temp
print(a, b)
a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)
a = 1
b = 2
c = 3
d = 4
print(a, b, c, d)
a, b, c, d = b, d, a, c
print(a, b, c, d)