class A:
    def process(self):
        print('Klasse A')

class B:
    def process(self):
        print('Klasse B')

class C(A, B):
    pass

obj = C()  
obj.process()    
print(C.mro())