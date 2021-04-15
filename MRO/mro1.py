class A: 
    i = 42
class B:
    i = 1
class C(A,B):
    def __init__(self, i):
        print(super().i)
        self.i = i

    def test(self):
        print(self.i)
C(7).test()