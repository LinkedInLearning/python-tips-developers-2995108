class Person:
    def auskunft(self):
        print("Mein Name ist",self.vname,self.nname)
    def __getVname(self): return self.__vname
    def __getNname(self): return self.__nname
    def __getGebdat(self): return self.__gebdat
    def __setVname(self,vname): self.__vname=vname
    def __setNname(self,nname): self.__nname=nname
    vname=property(__getVname,__setVname)
    nname=property(__getNname,__setNname)
    gebdat=property(__getGebdat,None)
    def __init__(self,vname,nname, gebdat):
        self.__vname=vname
        self.__nname=nname
        self.__gebdat=gebdat
class Podcast:
    def __init__(self,fname):
        self.__fname=fname
    fname=property(lambda self:self.__fname)
    def auskunft(self):
        print("Wir betreiben den Podcast",self.fname)
class Mitarbeiter(Podcast,Person):
    def __getPid(self):
        return self.__pid
    pid = property(__getPid,None)
    def __init__(self,vname,nname, gebdat,pid,fname):
         Person.__init__(self,vname,nname, gebdat)
         Podcast.__init__(self,fname)
         self.__pid=pid
        

p1 = Mitarbeiter("Florian","Roth","09.02.2000",1,"Harz und Herzlich")
p2 = Mitarbeiter("Felix","Roth","09.02.2000",2,"Harz und Herzlich")

print(p1.vname)
print(p2.vname)
p1.auskunft()
