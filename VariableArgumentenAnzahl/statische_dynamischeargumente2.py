def meine_summme(a,b,*args):
    result = 0
    for x in args:
        result += x
    return result
    

#ÜBERGABE VON PARAMETERN IN OBJEKTFORM¶
print(meine_summme(*(1, 2, 3)))

print(meine_summme(*[1, 2, 3]))
