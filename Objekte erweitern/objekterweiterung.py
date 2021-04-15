class Person():
    def __init__(self):
        self.alter = 34

obj1 = Person()
print("Das Dictionary __dict__:", obj1.__dict__,"\n")
obj1.name = "Herby"
print("Das Dictionary __dict__:", obj1.__dict__,"\n")
def reden():
    print("Hallo")
obj1.reden = reden
print("Das Dictionary __dict__:", obj1.__dict__,"\n")
obj1.reden()
obj1.singen = lambda x: print(x)
obj1.singen("Lala")
print("Das Dictionary __dict__:", obj1.__dict__,"\n")
