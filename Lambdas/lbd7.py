def aussen(n):
    i = 5
    return lambda x: x * n * i
algorit = aussen(2)
print(algorit(11))