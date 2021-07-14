z = 12345678
t = "Hallo Welt"
l = [2,3,5,7]

def fkt1(x):
    return x * 2
def fkt2(x):
    return int(x) * 2
a = map(fkt1,t)
print(a, type(a))
print(list(a))

b = map(fkt1,l)
print(b, type(b))
print(set(b))

c = map(fkt1,str(z))
print(c, type(c))
print(tuple(c))

d = map(fkt2,str(z))
print(d, type(d))
print(tuple(d))