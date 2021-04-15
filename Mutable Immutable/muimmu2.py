x = [1,2]
y = x
print (x, type(x), y, type(y))
print(id(x), id(y),id(x)== id(y), id(x)== id([1,2]), id(y)== id([1,2]), x is y)
x.append(3)
print (x, type(x), y, type(y))
print(id(x), id(y),id(x)== id(y), id(x)== id([1,2]), id(y)== id([1,2]), x is y)
