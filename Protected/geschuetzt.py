class A: 
    _i = 42
class B:
    _j = 1
class C(A,B):
    def __init__(self):
        print(super()._i)
        print(super()._j)

    def test(self):
        print(self._i)
        
C().test()
print(A()._i)