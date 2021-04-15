def a(x):
    if x < 5:
        return True
    else:
        return False
def b():
    return 42
lbd = lambda x: a(x) or b()
print(lbd(3))
print(lbd(4))
print(lbd(5))