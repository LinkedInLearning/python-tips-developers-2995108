def fkt1(a, b, c):
    return a * b + c * i
def fkt3(p1, *args):
    res = 0
    res += p1
    for i in args:
        res *= i
    return res
fkt4 = lambda x: x * 2
def fkt2(a, b, c):
    global i
    i += 1
    return a * b + c * i

i = 3
print(fkt1(3,5,7))
print(fkt2(3,5,7))
print(fkt3(3))
print(fkt3(3,5,7))
print(fkt4(3))


