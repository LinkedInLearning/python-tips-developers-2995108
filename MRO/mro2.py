class A:
    def process(self):
        print('Klasse A')

class B:
    pass

class C(A, B):
    pass

obj = C()  
obj.process()    
print(C.mro())