import sys
a = 1
b = (1,2,3,4)
c = [1,2,3,4]
class A:
    def meineMethode(self):
        pass
d = A()
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))