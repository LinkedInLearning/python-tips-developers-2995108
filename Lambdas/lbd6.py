def aussen(n):
    return lambda x: x *n 
verdoppeln = aussen(2)
print(verdoppeln(11))