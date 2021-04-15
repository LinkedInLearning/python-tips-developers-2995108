def meine_funktion(p1, p2, *args ,**kwargs):
    print("Wert von p1: ", p1, ":", "Typ von p1", type(p1))
    print("Wert von p2: ", p2, ":","Typ von p2", type(p2))
    print("Wert von args: ", args, ":","Typ von args", type(args))
    print("Wert von kwargs: ", kwargs, ":","Typ von kwargs", type(kwargs))
    print("*" * 50)
    
    

meine_funktion('A',*(100,200,300))
meine_funktion('A',**{'p2':1000})
meine_funktion(p2 = 1000, *('A',))
meine_funktion(1,2,*(100,200,300),c=1)
meine_funktion(1,2,c=1, d= 2)