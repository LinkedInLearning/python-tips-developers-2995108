class Auto:
    def __init__(self):
        self.typ = "PKW"
        self.motor = self.Motor()
        self.getriebe = self.Getriebe()

    class Motor:
        ps = 100
    class Getriebe:
        anzahl_gaenge = 6

kfz = Auto()
print(kfz.motor.ps)
print(kfz.getriebe.anzahl_gaenge)
