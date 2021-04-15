class Person:
    def __getName(self):
        return self.__name
    def __setName(self,name):
        self.__name=name
    def __init__(self,name):
        self.__name=name
    NAME = property(__getName)

x = Person("Hans")
print(x.NAME)
x.NAME = "Otto"
