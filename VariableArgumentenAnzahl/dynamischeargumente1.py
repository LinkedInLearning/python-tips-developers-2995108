def meine_summme(*args):
    result = 0
    print(type(args))
    for x in args:
        result += x
    return result
    


print(meine_summme(1, 2, 3))

