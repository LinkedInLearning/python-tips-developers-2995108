class Hund:
    pass
class Katze:
    pass

def lautGeben(o):
    if isinstance(o,Hund):
        print("Wau")
    elif isinstance(o,Katze):
        print("Miau")  

lautGeben(Hund())  
lautGeben(Katze()) 