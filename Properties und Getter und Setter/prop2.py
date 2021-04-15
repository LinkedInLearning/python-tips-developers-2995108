class SuperDopper:
    def __init__(self):
        self.x=42
class Person(SuperDopper):
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
    Nname = property(__getNName,__setNName)
    Vname = property(__getVName,__setVName)
    Gebdat = property(__getGebdat,None)
    
    def __init__(self,nname,vname,gebdat):
        self.__nname=nname
        self.__vname=vname
        self.__gebdat=gebdat

class Firma(SuperDopper):
    def __init__(self,eigentuemer):
        self.__eigentuemer=eigentuemer
    def __getEigentuemer(self):
        return self.__eigentuemer
    Eigentuemer=property(__getEigentuemer,None)

class Mitarbeiter (Person,Firma):
    
    def __getPersid(self):
        return self.__persid
    Persid = property(__getPersid,None)
    def __init__(self,nname,vname,gebdat,eigentuemer,persid):
        SuperDopper.__init__(self)
        Person.__init__(self,nname,vname,gebdat)
        Firma.__init__(self,eigentuemer)
        self.__persid=persid

p = Mitarbeiter("Meier","Hans","12.09.1976","Will Wuest",1007)
print(p.Persid, p.Nname,p.Eigentuemer,p.x)
