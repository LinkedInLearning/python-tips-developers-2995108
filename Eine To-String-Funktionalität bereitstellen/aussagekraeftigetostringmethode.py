class Person:
    def __init__(self,alter,vname,nname):
        self.alter=alter
        self.vname=vname
        self.nname=nname 
    def __str__(self):
        temp = ""
        for k,v in self.__dict__.items():
            temp += str(k) + " : " + str(v) + "\n"
        return temp


p1 = Person(50,"Hans", "Dampf")
print(p1)
p2 = Person(45,"Fred", "Feuerstein")
print(p2)