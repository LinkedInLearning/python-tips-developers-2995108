class Hund:
    def lautGeben(self):
        print("Wau")
class Katze:
    def lautGeben(self):
        print("Miau")

def lautGeben(o):
    o.lautGeben()

lautGeben(Hund())  
lautGeben(Katze()) 