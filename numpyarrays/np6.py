import numpy as np
a = np.array(np.arange(10))
b = np.array(np.arange(10,20))
c = np.array([[1, 2], [3, 4]])
d = np.array([[5, 6], [7, 8]])
print("Multiplikation von {} * {} :\t{}\n".format(a,b,a * b))
print("Multiplikation von {} * {} :\t{}\n".format(c,d,c * d))
print("Division von {} * {} :\t{}\n".format(a,b,a / b))
print("Division von {} * {} :\t{}\n".format(c,d,c / d))
