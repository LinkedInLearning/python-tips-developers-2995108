class Auto:
    def __init__(self):
        self.typ = "PKW"
        self.motor = self.__Motor()
        self.getriebe = self.__Getriebe()

    class __Motor:
        ps = 100
    class __Getriebe:
        anzahl_gaenge = 6

print(Auto().motor.ps)