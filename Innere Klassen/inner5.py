class Auto:
    
    def __init__(self):
        self.typ = "PKW"
        self.motor = self.Motor()
        self.getriebe = self.Getriebe()

    class Motor:
        ps = 100
        def typabfrage(self):
            print(eigentuemer)
    class Getriebe:
        anzahl_gaenge = 6

class SUV(Auto):
    def __init__(self):
        self.typ = "SUV"
        self.farbe = "Rot"
        self.motor = self.Motor()
        self.getriebe = self.Getriebe()

a = SUV()
print(a.farbe)
print(a.getriebe.anzahl_gaenge)