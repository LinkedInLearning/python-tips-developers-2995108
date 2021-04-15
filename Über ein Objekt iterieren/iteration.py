class Person:
    def __init__(self,alter,vname,nname,konto):
        self.alter=alter
        self.vname=vname
        self.konto=konto
        self.nname=nname    
   

class Konto:
    def __init__(self,kontonr, betrag):
        self.kontonr=kontonr
        self.__betrag=betrag
    def einzahlen(self,betrag):
        self.__betrag+=betrag
        
    def auszahlen(self,betrag):    
        if self.__betrag - betrag >= 0:
            self.__betrag-=betrag
        else:
            self.__betrag = 0
    def getBetrag(self):
        return self.__betrag     

p1 = Person(50,"Hans", "Dampf", Konto(4711,1000))
print(p1.__dict__)
for k in p1.__dict__:
    print(k)
for k in p1.__dict__:
    print(k, p1.__dict__[k])
for v in p1.__dict__.values():
    print(v)
print(p1.__dict__.items())
for k,v in p1.__dict__.items():
    print(k,v)