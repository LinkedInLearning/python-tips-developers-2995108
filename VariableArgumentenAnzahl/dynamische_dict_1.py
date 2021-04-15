def meine_summme(**kwargs):
    result = 0
    print(type(kwargs))
    for x in kwargs.values():
        result += x
    return result
    


print(meine_summme(a=1, b=2, c=3))

