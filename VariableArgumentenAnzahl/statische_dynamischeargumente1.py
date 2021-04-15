def meine_summme(a,b,*args):
    result = 0
    
    for x in args:
        result += x
    return result
    


print(meine_summme(1, 2, 3, 4, 5))

