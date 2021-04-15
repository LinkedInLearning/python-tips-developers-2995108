x = 1
y = x
print(x, type(x), y, type(y))
print(id(x), id(y), id(x)==id(y), id(x) == id(1), id(y) == id(1), x is y)
x += 1
print(x, type(x), y, type(y))
print(id(x), id(y), id(x)==id(y), id(x) == id(1), id(y) == id(1), x is y)
