class A:
    def process(self):
        print('Klasse A')

class B:
    def process(self):
        print('Klasse B')

class C(A,B):
    def process(self):
        print('Klasse C')

class D(B,C): # MRO ist nicht eindeutig -> Fehler
    pass

obj = D()  
obj.process()    
print(C.mro())