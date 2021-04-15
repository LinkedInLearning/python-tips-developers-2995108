class Tier():
    __slots__ = ['alter','name']
    def __init__(self):
        self.alter = 5

obj1 = Tier()
print(obj1.alter)
print(obj1.__slots__)
obj1.name="Herby"
print(obj1.__slots__)
print(obj1.name)


