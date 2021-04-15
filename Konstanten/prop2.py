class A:
    def __init__(self,name):
        self.__name=name
    NAME=property(lambda self:self.__name)


o1 = A("Otto")
print("Zugriff über Property %s." % o1.NAME)



