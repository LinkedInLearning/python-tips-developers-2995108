import numpy as np
a = np.array(np.arange(10))
b = np.array([2,3,5,7,11,15])
print(type(a), a,a.shape)
print(type(b), b, b.shape)
c = np.concatenate((a, b))
print(type(c), c, c.shape)
