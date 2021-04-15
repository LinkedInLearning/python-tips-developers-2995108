class Person:
    def __getGebdat(self):
        return self.__gebdat
    def __getNName(self):
        return self.__nname
    def __setNName(self,nname):
        self.__nname=nname
    def __getVName(self):
        return self.__vname
    def __setVName(self,vname):
        self.__vname=vname
    def __init__(self,nname,vname,gebdat):
        self.__nname=nname
        self.__vname=vname
        self.__gebdat=gebdat
    Nname = property(__getNName,__setNName)
    Vname = property(__getVName,__setVName)
    Gebdat = property(__getGebdat)

x = Person("Meier","Hans","17.09.1998")
print(x.Nname, x.Vname, x.Gebdat)
